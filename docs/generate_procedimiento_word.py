from pathlib import Path

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "docs" / "procedimiento_actualizacion_repositorio.docx"
REPOSITORY_URL = "https://github.com/Ericklies/develcd9614709.git"


def add_code(document: Document, source: str) -> None:
    paragraph = document.add_paragraph(style="Code Block")
    paragraph.add_run(source)
    shading = OxmlElement("w:shd")
    shading.set(qn("w:fill"), "F1F4F7")
    paragraph._p.get_or_add_pPr().append(shading)


def add_inline_code(paragraph, text: str) -> None:
    run = paragraph.add_run(text)
    run.font.name = "Consolas"
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(35, 55, 75)


def add_numbered_section(document: Document, title: str, paragraphs: list[str]) -> None:
    document.add_heading(title, level=1)
    for text in paragraphs:
        document.add_paragraph(text)


def build_document() -> None:
    document = Document()
    section = document.sections[0]
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)
    section.left_margin = Inches(0.85)
    section.right_margin = Inches(0.85)

    styles = document.styles
    styles["Normal"].font.name = "Aptos"
    styles["Normal"].font.size = Pt(10)
    styles["Title"].font.name = "Aptos Display"
    styles["Title"].font.size = Pt(26)
    styles["Title"].font.color.rgb = RGBColor(35, 68, 105)
    styles["Heading 1"].font.name = "Aptos Display"
    styles["Heading 1"].font.color.rgb = RGBColor(35, 68, 105)
    styles["Heading 2"].font.name = "Aptos Display"
    styles["Heading 2"].font.color.rgb = RGBColor(25, 115, 115)

    code_style = styles.add_style("Code Block", WD_STYLE_TYPE.PARAGRAPH)
    code_style.font.name = "Consolas"
    code_style.font.size = Pt(9)
    code_style.paragraph_format.left_indent = Inches(0.18)
    code_style.paragraph_format.space_before = Pt(3)
    code_style.paragraph_format.space_after = Pt(8)

    title = document.add_heading("Procedimiento de actualización del repositorio", 0)
    title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    subtitle = document.add_paragraph("Proyecto #1 | EDA - Predict Future Sales")
    subtitle.style = "Subtitle"
    document.add_paragraph(f"Repositorio: {REPOSITORY_URL}")

    document.add_heading("Índice", level=1)
    index_entries = [
        "1. Requisitos previos",
        "2. Clonar el repositorio por primera vez",
        "3. Configurar usuario y correo de Git",
        "4. Flujo diario: rama, cambios y Pull Request",
        "5. Resolver conflictos básicos",
        "6. Evitar subir datos pesados o credenciales",
        "7. Actualizar el clon o sincronizar un fork",
        "8. Buenas prácticas de commits",
        "9. Evidencia de git pull: screenshots",
    ]
    for entry in index_entries:
        document.add_paragraph(entry)

    add_numbered_section(
        document,
        "1. Requisitos previos",
        [
            "Instala Git y comprueba su disponibilidad desde una terminal.",
            "Necesitas una cuenta de GitHub y permiso de lectura/escritura en el repositorio del equipo.",
            "Configura SSH o HTTPS con Git Credential Manager. Nunca incluyas tokens ni contraseñas en comandos guardados, capturas o commits.",
        ],
    )
    add_code(document, "git --version")

    add_numbered_section(
        document,
        "2. Clonar el repositorio por primera vez",
        [
            "Abre PowerShell o una terminal, navega a la carpeta donde guardarás el proyecto y clona el remoto:",
        ],
    )
    add_code(document, f"git clone {REPOSITORY_URL}\ncd develcd9614709")
    document.add_paragraph("Verifica la rama principal y trae su estado actual:")
    add_code(document, "git switch main\ngit pull origin main\ngit status")

    add_numbered_section(
        document,
        "3. Configurar usuario y correo de Git",
        [
            "Configura el nombre y el correo que aparecerán como autoría de tus commits. Usa el correo asociado a tu cuenta de GitHub o el correo noreply que GitHub te proporciona.",
        ],
    )
    add_code(
        document,
        'git config --global user.name "Tu Nombre"\n'
        'git config --global user.email "tu-correo@example.com"\n'
        "git config --global --list",
    )
    document.add_paragraph("La opción --global aplica a todos tus repositorios. Omítela si deseas configurar esta identidad solo en el repositorio actual.")

    add_numbered_section(
        document,
        "4. Flujo diario: rama, cambios y Pull Request",
        [
            "Actualiza main antes de empezar. Crea una rama propia para cada tarea y evita trabajar directamente sobre main:",
        ],
    )
    add_code(
        document,
        "git switch main\n"
        "git pull origin main\n"
        "git checkout -b feat/mi-cambio\n"
        "# Realiza y prueba tus cambios\n"
        "git status\n"
        "git add .\n"
        'git commit -m "feat: describe el cambio"\n'
        "git push origin feat/mi-cambio",
    )
    document.add_paragraph("En GitHub, abre un Pull Request desde feat/mi-cambio hacia main. Describe el cambio, enlaza cualquier incidencia y espera las revisiones antes de integrar.")

    add_numbered_section(
        document,
        "5. Resolver conflictos básicos",
        [
            "Un conflicto ocurre cuando dos ramas cambian líneas que Git no puede combinar automáticamente. Comprueba los archivos afectados y abre cada uno para resolver los marcadores <<<<<<<, ======= y >>>>>>>.",
        ],
    )
    add_code(
        document,
        "git status\n"
        "# Edita los archivos y conserva la versión correcta\n"
        "git add ruta/al/archivo\n"
        'git commit -m "chore: resolver conflictos de integración"',
    )
    document.add_paragraph("Si estabas integrando con merge y prefieres cancelar la operación, ejecuta git merge --abort. Después de resolver, vuelve a ejecutar las pruebas pertinentes.")

    add_numbered_section(
        document,
        "6. Evitar subir datos pesados o credenciales",
        [
            "Los archivos Kaggle se guardan en data/raw/ y no se versionan. El .gitignore del proyecto excluye data/, entornos virtuales, archivos .env, checkpoints de Jupyter y kaggle.json.",
            "Antes de confirmar, inspecciona el conjunto exacto de archivos. No uses git add -f para forzar datos o credenciales al repositorio.",
        ],
    )
    add_code(document, "git status --short\ngit check-ignore -v data/raw/sales_train.csv kaggle.json .env")

    add_numbered_section(
        document,
        "7. Actualizar el clon o sincronizar un fork",
        [
            "Para un clon directo del repositorio del equipo, actualiza main antes de cada tarea y luego integra sus cambios en tu rama:",
        ],
    )
    add_code(document, "git switch main\ngit pull origin main\ngit switch feat/mi-cambio\ngit merge main")
    document.add_paragraph("Si trabajas desde un fork, configura el repositorio original como upstream una sola vez y sincroniza desde él:")
    add_code(
        document,
        "git remote add upstream https://github.com/Ericklies/develcd9614709.git\n"
        "git fetch upstream\n"
        "git switch main\n"
        "git merge upstream/main\n"
        "git push origin main",
    )

    add_numbered_section(
        document,
        "8. Buenas prácticas de commits",
        [
            "Usa commits pequeños, enfocados y escritos en modo imperativo. Sigue Conventional Commits para que el propósito sea claro:",
        ],
    )
    add_code(
        document,
        'feat: agregar heatmap por sucursal\n'
        'fix: corregir conversión de fechas\n'
        'docs: documentar el flujo de git pull\n'
        'test: validar el cálculo de cobertura de test\n'
        'chore: actualizar dependencias del análisis',
    )

    add_numbered_section(
        document,
        "9. Evidencia de git pull: screenshots",
        [
            "Cada integrante debe ejecutar git pull origin main y guardar una captura donde se vean el comando y el resultado exitoso. Guarda un archivo PNG por persona en docs/screenshots/<nombre_integrante>.png.",
            "Añade la captura a tu Pull Request. Revisa que no muestre tokens, contraseñas, información personal ni otras ventanas privadas.",
        ],
    )
    add_code(document, "docs/screenshots/erick.png\ndocs/screenshots/otro_integrante.png")

    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.add_run("EDA - Predict Future Sales | Colaboración Git")

    document.save(OUTPUT_PATH)
    print(f"Documento generado: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_document()