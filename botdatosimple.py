import os
import io
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Configurar matplotlib para servidores sin interfaz gráfica (EVITA ERRORES EN RENDER)
matplotlib.use('Agg')

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener el token y la URL de Render de forma segura
TOKEN = os.getenv("BotDataSimple_Token")
RENDER_URL = os.getenv("URL_RENDER", "https://Proyecto-Analisis-Descriptivo-CSV-ChatbotTelegram-PY.onrender.com")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! Soy tu bot analista de datos 🤖.\n\n"
        "Para comenzar, por favor envíame un archivo en formato **.csv** con tus datos. "
        "Me encargaré de estandarizar la información y generar el reporte."
    )

async def recibir_documento(update: Update, context: ContextTypes.DEFAULT_TYPE):
    documento = update.message.document
    
    # Validar que sea un archivo CSV
    if not documento.file_name.endswith('.csv'):
        await update.message.reply_text("⚠️ Por favor, envíame un archivo con extensión .csv")
        return

    await update.message.reply_text("⏳ Descargando y analizando tu documento, por favor espera...")

    try:
        # Descargar el archivo directamente en la memoria RAM
        file = await context.bot.get_file(documento.file_id)
        file_bytes = await file.download_as_bytearray()
        
        # Leer el CSV con pandas
        df = pd.read_csv(io.BytesIO(file_bytes))
        
        # Estandarizar columnas
        if len(df.columns) < 2:
            await update.message.reply_text("⚠️ El archivo debe tener al menos dos columnas (ej: Empleado y Ventas).")
            return
            
        col_empleado = df.columns[0]
        col_ventas = df.columns[1]

        # Asegurar que la columna de ventas sea numérica
        df[col_ventas] = pd.to_numeric(df[col_ventas], errors='coerce')
        df = df.dropna(subset=[col_ventas]) 

        # --- PARTE 1: Crear columna de clasificación ---
        def clasificar_rendimiento(ventas):
            if ventas >= 55:
                return "Alto rendimiento"
            elif 50 <= ventas <= 54:
                return "Rendimiento medio"
            else:
                return "Bajo rendimiento"

        df['Clasificación'] = df[col_ventas].apply(clasificar_rendimiento)

        # --- PARTE 2: Estadística Descriptiva ---
        media = df[col_ventas].mean()
        mediana = df[col_ventas].median()
        moda = df[col_ventas].mode()[0] if not df[col_ventas].mode().empty else "N/A"
        std = df[col_ventas].std()
        max_v = df[col_ventas].max()
        min_v = df[col_ventas].min()

        empleado_max = df.loc[df[col_ventas].idxmax(), col_empleado]
        empleado_min = df.loc[df[col_ventas].idxmin(), col_empleado]

        mensaje_analisis = (
            f"📊 *REPORTE DE DATOS: {documento.file_name}*\n\n"
            "*1. ESTADÍSTICA DESCRIPTIVA:*\n"
            f"• Media (Promedio): {media:.2f}\n"
            f"• Mediana: {mediana:.2f}\n"
            f"• Moda: {moda}\n"
            f"• Desviación Estándar: {std:.2f}\n"
            f"• Valor Máximo: {max_v} ({empleado_max})\n"
            f"• Valor Mínimo: {min_v} ({empleado_min})\n\n"
            "*2. INTERPRETACIÓN:*\n"
            f"• Las métricas indican que el centro de los datos se ubica alrededor de {media:.2f}.\n"
            f"• Una desviación estándar de {std:.2f} muestra el nivel de dispersión general de los empleados frente al promedio.\n\n"
            "*3. RENDIMIENTO DESTACADO:*\n"
            f"• *Mayor rendimiento:* {empleado_max} lidera con {max_v}.\n"
            f"• *Menor rendimiento:* {empleado_min} registró {min_v}."
        )

        await update.message.reply_text(mensaje_analisis, parse_mode='Markdown')

        # --- PARTE 3: Visualización ---
        plt.figure(figsize=(10, 6))
        
        colores = ['#ff9999' if x < 50 else '#66b3ff' if x < 55 else '#99ff99' for x in df[col_ventas]]
        
        plt.bar(df[col_empleado].astype(str), df[col_ventas], color=colores)
        plt.title(f'{col_ventas} por {col_empleado}')
        plt.xlabel(col_empleado)
        plt.ylabel(col_ventas)
        plt.axhline(media, color='red', linestyle='dashed', linewidth=2, label=f'Promedio ({media:.2f})')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.legend()
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()

        await update.message.reply_photo(photo=buf, caption="📈 Gráfico de distribución. La línea roja marca el promedio.")

    except Exception as e:
        await update.message.reply_text(f"❌ Ocurrió un error al procesar el archivo. Revisa el formato: {e}")

async def responder_texto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Por favor, envíame un archivo .csv arrastrándolo al chat para generar el análisis.')

if __name__ == '__main__':
    if not TOKEN:
        print("Error: No se encontró el BotDataSimple_Token en el archivo .env")
    else:
        # Asignación de puerto dinámico para Render
        PORT = int(os.environ.get('PORT', 10000))

        app = ApplicationBuilder().token(TOKEN).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.Document.ALL, recibir_documento))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_texto))

        print("Iniciando DataSimpleBot en modo Webhook... 📊")
        
        # Ejecución mediante Webhook
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            webhook_url=f"{RENDER_URL}/{TOKEN}",
            url_path=TOKEN
        )