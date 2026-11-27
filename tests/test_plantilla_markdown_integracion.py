from chuspacalc.io.exportador_markdown import exportar_markdown
from chuspacalc.io.plantilla_exportacion import PlantillaExportacion


def test_plantilla_md_corresponde_a_exportador_markdown_funcional() -> None:
    plantilla = PlantillaExportacion(formato="md")

    contenido = exportar_markdown("Viga", {"L": 5}, 12.5, unidad="kN")

    assert plantilla.formato == "md"
    assert contenido.startswith("# Viga\n")
    assert "| L | 5 |" in contenido
    assert "12.5 kN" in contenido
