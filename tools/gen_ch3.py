#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera sections/cap03/00_profesional.tex (Perfil Profesional)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import genlib as g

P = "ethoshub-profesional"

# --- Educación: orden didáctico explícito + leyendas -------------------------
EDU = [
 ("barra_lateral_profesional_educacion.png", "Para entrar al apartado, haga clic en \\boton{Educación} (icono de gorra de graduado) en el panel lateral izquierdo."),
 ("Pagina_Principal_de_Educacion.png", "Vista principal del apartado \\campo{Educación}, donde se concentra todo su historial académico."),
 ("Panel_Superior_Registra_Titulos.png", "El panel superior resume el número de títulos, los años de formación y la cantidad de centros registrados."),
 ("Panel_inferior_Historial_acedemico.png", "Para iniciar un registro pulse \\boton{Historial académico} (arriba a la derecha) o el botón que aparece dentro del panel cuando aún no existe ningún registro."),
 ("Formulacio_registro_Nueva_trayectoria_vacio.png", "Al pulsar cualquiera de los botones se abre el formulario \\campo{Nueva trayectoria}. Los campos marcados con asterisco (*) son obligatorios."),
 ("Formulacio_registro_Nueva_trayectoria_01.png", "En el campo \\campo{Institución} escriba el nombre del centro donde se formó o estudia actualmente."),
 ("Formulacio_registro_Nueva_trayectoria_02.png", "El campo \\campo{Tipo de educación} permite seleccionar la modalidad de estudios mediante un desplegable."),
 ("Formulacio_registro_Nueva_trayectoria_02a.png", "Al desplegar \\campo{Tipo de educación} se muestran las opciones disponibles para clasificar la formación."),
 ("Educacion_combobox_tipo_educacion.png", "Seleccione en el desplegable el tipo de educación que corresponda a su trayectoria."),
 ("Formulacio_registro_Nueva_trayectoria_03.png", "En \\campo{Título/Grado} indique el nombre del título o grado obtenido o en curso."),
 ("Formulacio_registro_Nueva_trayectoria_04.png", "En \\campo{Área de estudio} especifique la especialidad o el área concreta de la formación."),
 ("Formulacio_registro_Nueva_trayectoria_05.png", "En \\campo{Inicio y fin} registre las fechas de comienzo y conclusión de los estudios."),
 ("Formulacio_registro_Nueva_trayectoria_05a.png", "Al abrir el selector de fechas puede navegar por meses y años para elegir la fecha de inicio."),
 ("Formulacio_registro_Nueva_trayectoria_05b.png", "El calendario permite seleccionar el día exacto de inicio de la formación."),
 ("Formulacio_registro_Nueva_trayectoria_05c.png", "De igual forma, el selector de fecha de fin se despliega como un calendario interactivo."),
 ("Formulacio_registro_Nueva_trayectoria_05d.png", "Elija el mes y el año correspondientes a la fecha de finalización."),
 ("Formulacio_registro_Nueva_trayectoria_05e.png", "Confirme el día seleccionado para registrar la fecha de fin."),
 ("Formulacio_registro_Nueva_trayectoria_06.png", "En \\campo{Promedio/GPA} introduzca la calificación obtenida, siguiendo el ejemplo que sugiere el sistema."),
 ("Formulacio_registro_Nueva_trayectoria_07.png", "En \\campo{Link de verificación} pegue la dirección web del centro o de la credencial que acredita la formación."),
 ("Formulacio_registro_Nueva_trayectoria_08.png", "Active la casilla \\campo{Estudio actualmente} si la formación sigue en curso."),
 ("Formulario_Bloqueo_Fin_fecha.png", "Al activar \\campo{Estudio actualmente}, el campo de fecha de fin se bloquea automáticamente, ya que no procede indicarla."),
 ("Formulacio_registro_Nueva_trayectoria_09.png", "En \\campo{Logo institución} puede subir el logotipo del centro desde un archivo local."),
 ("Formulacio_registro_Nueva_trayectoria_09a.png", "Al pulsar \\boton{Subir archivo} se abre el explorador de archivos para seleccionar la imagen del logotipo."),
 ("Educacion_subir_logo_url.png", "Como alternativa, pulse \\boton{URL} para cargar el logotipo a partir de una dirección web."),
 ("Educacion_subir_logo_url_01.png", "Pegue la URL del logotipo; el sistema mostrará una previsualización de la imagen."),
 ("Formulacio_registro_Nueva_trayectoria_10.png", "En \\campo{Certificado/Título} puede subir el documento (imagen o PDF) que respalda la formación."),
 ("Formulacio_registro_Nueva_trayectoria_10a.png", "Al pulsar \\boton{Subir archivo} se abre el explorador para seleccionar el certificado desde su equipo."),
 ("Educacion_subir_pdf_url.png", "También puede pulsar \\boton{URL} para enlazar el certificado mediante una dirección web."),
 ("Educacion_subir_pdf_url_01.png", "Introduzca la URL del certificado para vincularlo al registro."),
 ("Formulacio_registro_Nueva_trayectoria_11.png", "Una vez completado el formulario, use \\boton{Cancelar} para descartar o \\boton{Guardar} para registrar la trayectoria."),
 ("Formulacio_registro_Nueva_trayectoria_11a.png", "El botón \\boton{Guardar} confirma y almacena el nuevo registro de formación."),
 ("Formulacio_registro_Nueva_trayectoria_11b.png", "El botón \\boton{Cancelar} cierra el formulario sin guardar los datos introducidos."),
 ("Educacion_panel_principal_registrado.png", "Tras guardar, la nueva trayectoria aparece reflejada en la página de Educación."),
 ("Educacion_Contador_de_registro.png", "El panel superior se actualiza: aumentan los contadores de títulos, años (calculados automáticamente a partir de las fechas) y centros."),
 ("Profesional_Educacion_registrado.png", "El historial académico muestra la trayectoria registrada en formato de listado."),
 ("Profesional_Educacion_registrado_01.png", "Cada registro presenta sus datos principales de forma resumida y ordenada."),
 ("Educacion_vista_previa_de_registro.png", "Al seleccionar un registro, a la derecha se despliega un panel con la previsualización de todos los campos completados."),
 ("Educacion_vista_previa_de_registro01.png", "Desde la vista previa puede pulsar el botón de edición para modificar cualquier campo del registro."),
 ("Educacion_vista_previa_de_registro02.png", "El enlace de verificación de credencial permite acceder al sitio web indicado en el formulario."),
 ("Educacion_vista_previa_de_registro03.png", "En \\campo{Certificado adjunto} puede visualizar o descargar la imagen o el PDF cargado."),
 ("Educacion_vista_previa_de_registro04.png", "El botón de eliminación retira la certificación adjunta del registro."),
 ("Profesional_Educacion_registrado_02.png", "Desde la página principal también puede editar el historial académico con el botón de edición."),
 ("Profesional_Educacion_registrado_03.png", "El botón de papelera permite eliminar un registro del historial académico."),
 ("Educacion_eliminar_registro.png", "Antes de borrar, el sistema solicita confirmación con las opciones \\boton{Cancelar} y \\boton{Eliminar}."),
]

# --- CV Studio: CAP1..CAP30 (orden natural) ----------------------------------
CV = [
 "Acceda a \\boton{CV Studio} desde el panel lateral izquierdo para abrir el estudio de currículum, con sus botones, plantillas y editor.",
 "El estudio ofrece dos formatos de trabajo: \\boton{LaTeX} y \\boton{Markdown}. En primer lugar seleccionamos \\boton{LaTeX}.",
 "Dentro de las plantillas LaTeX seleccionamos \\campo{Moderno Pro}, que abre el editor con el contenido de la plantilla.",
 "Vista ampliada del editor de la plantilla \\campo{Moderno Pro}.",
 "Seleccionamos ahora la plantilla LaTeX \\campo{Ejecutivo Clásico}, que también dispone de su propio editor.",
 "Vista ampliada del editor de la plantilla \\campo{Ejecutivo Clásico}.",
 "Seleccionamos la plantilla LaTeX \\campo{Compacto Una Página} y se abre su editor correspondiente.",
 "Vista ampliada del editor de la plantilla \\campo{Compacto Una Página}.",
 "Volvemos al selector de formato y ahora elegimos \\boton{Markdown}.",
 "Dentro de las plantillas Markdown seleccionamos \\campo{Ingeniero Senior}; el editor muestra su contenido.",
 "Vista ampliada del editor de \\campo{Ingeniero Senior}; arriba a la derecha el zoom está al 100\\,\\%.",
 "Seleccionamos la plantilla Markdown \\campo{Stack \\& Proyectos} y se abre su editor.",
 "Vista ampliada del editor de \\campo{Stack \\& Proyectos}; el zoom está al 75\\,\\%.",
 "Seleccionamos la plantilla Markdown \\campo{Minimalista Senior} y se abre su editor.",
 "Vista ampliada del editor de \\campo{Minimalista Senior}; el zoom está al 100\\,\\%.",
 "Al pulsar \\boton{Nuevo CV} comenzamos un currículum desde cero en Markdown, con las mismas plantillas disponibles.",
 "Al pulsar \\boton{Nuevo CV} también podemos empezar desde cero en LaTeX, con las plantillas LaTeX disponibles.",
 "El botón con icono de hojas pequeñas copia el código del editor al portapapeles.",
 "Al pulsar \\boton{Asistente IA} se abre una ventana de asistencia con inteligencia artificial.",
 "En esta ventana podemos elegir entre las opciones sugeridas o escribir directamente la solicitud para enviarla a la IA.",
 "Solicitamos a la IA un nuevo CV para un perfil de ingeniero en sistemas y la herramienta genera el código correspondiente.",
 "El botón \\boton{Aplicar al editor} carga automáticamente el resultado de la IA en nuestro editor.",
 "Se muestra el nuevo CV generado por la IA; arriba a la derecha el zoom está al 75\\,\\%.",
 "Al pulsar \\boton{Exportar} podemos elegir el formato de exportación del currículum.",
 "En el menú \\boton{Exportar} seleccionamos \\boton{Exportar PDF}.",
 "Tras pulsar \\boton{Exportar PDF}, el documento se genera y se descarga en formato PDF.",
 "La opción \\boton{Exportar Markdown} genera el archivo de la misma forma que la exportación a PDF.",
 "La opción \\boton{Exportar TXT} descarga el currículum en texto plano, igual que las exportaciones anteriores.",
 "Al pulsar \\boton{Guardar en mi perfil} se abre una ventana que solicita confirmar o cancelar la acción.",
 "En la ventana \\campo{Guardar documento} escribimos el nombre deseado y pulsamos \\boton{Guardar} para almacenarlo en el perfil.",
]

# --- Responsive: pares (archivo, leyenda) ------------------------------------
RESP = [
 ("profesional_responsive_mi_portafolio.jpg", "Mi portafolio en vista móvil."),
 ("profesional_responsive_habilidades.jpg", "Apartado de Habilidades en vista móvil."),
 ("profesional_responsive_habilidades_hard.jpg", "Alta de una habilidad técnica (hard skill) en móvil."),
 ("profesional_responsive_habilidades_soft.jpg", "Alta de una habilidad blanda (soft skill) en móvil."),
 ("profesional_responsive_proyectos.jpg", "Apartado de Proyectos en vista móvil."),
 ("profesional_responsive_formulario_proyectos.jpg", "Formulario de creación de proyecto en móvil."),
 ("profesional_responsive_experiencia.jpg", "Apartado de Experiencia en vista móvil."),
 ("profesional_responsive_formulario_experiencia.jpg", "Formulario de experiencia en móvil (parte 1)."),
 ("profesional_responsive_formulario_experiencia2.jpg", "Formulario de experiencia en móvil (parte 2)."),
 ("profesional_responsive_educacion.jpg", "Apartado de Educación en vista móvil."),
 ("profesional_responsive_formulario_educacion.jpg", "Formulario de educación en móvil (parte 1)."),
 ("profesional_responsive_formulario_educacion2.jpg", "Formulario de educación en móvil (parte 2)."),
 ("profesional_responsive_CVstudio.jpg", "CV Studio en vista móvil."),
 ("profesional_responsive_chat.jpg", "Bandeja de chat en vista móvil."),
 ("profesional_responsive_chat_iniciado.jpg", "Conversación de chat iniciada en móvil."),
 ("profesional_responsive_conexiones.jpg", "Apartado de Conexiones en vista móvil."),
 ("profesional_responsive_configuracion.jpg", "Configuración en vista móvil."),
 ("profesional_responsive_configuracion_campos.jpg", "Edición de campos de configuración en móvil."),
 ("profesional_responsive_configuracion_personalizacion.jpg", "Pestaña de Personalización en móvil."),
 ("profesional_responsive_configuracion_seguridad.jpg", "Pestaña de Seguridad en móvil."),
 ("profesional_responsive_barra_lateral.jpg", "Menú lateral desplegable en vista móvil."),
]

PROY = ("ethoshub-profesional/03_proyectos", "CrearProyecto",
        "ethoshub-profesional/03_proyectos/Proyecto.txt")
EXP = ("ethoshub-profesional/04_experiencia", "profesional_experiencia_laboral_",
       "ethoshub-profesional/04_experiencia/descripcion imagenes-profesional-experiencia.txt")
HAB = ("ethoshub-profesional/02_habilidades", "profesional_habilidades_",
       "ethoshub-profesional/02_habilidades/Habilidades.txt")
CFG = ("ethoshub-profesional/09_configuracion", "configuracion_profesional_",
       "ethoshub-profesional/09_configuracion/Configuracion Profesional.txt")

def bt(spec, rng=None):
    return g.block_from_txt(spec[0], spec[1], spec[2], rng)

OUT = []
A = OUT.append

A(r"""% =============================================================================
% CAPÍTULO 3 — GUÍA OPERATIVA: PERFIL PROFESIONAL  (generado por tools/gen_ch3.py)
% =============================================================================
\chapter{Guía Operativa: Perfil Profesional}
\label{ch:profesional}
\resumenCapitulo{Este capítulo guía a la persona usuaria con perfil Profesional en la
construcción y gestión de su portafolio digital: proyectos, experiencia laboral,
formación académica, habilidades y currículum, así como en la configuración y la
privacidad de su perfil público y el acceso desde dispositivos móviles.}

\section{Visión General del Espacio de Trabajo (Dashboard)}
\label{sec:prof-dashboard}
Tras iniciar sesión como Profesional, accederá a su espacio de trabajo. Desde el
\textbf{panel lateral izquierdo} se navega a todas las secciones del portafolio:
\campo{Mi portafolio}, \campo{Habilidades}, \campo{Proyectos}, \campo{Experiencia},
\campo{Educación}, \campo{CV Studio}, \campo{Conexiones}, \campo{Chat} y
\campo{Configuración}. El área central muestra el contenido de la sección activa y los
indicadores resumen (número de proyectos, habilidades destacadas, etc.).

\begin{AvisoNota}
El portafolio se construye por bloques independientes. Puede completarlos en el orden
que prefiera; cada bloque se guarda por separado y se refleja de inmediato en su perfil
público.
\end{AvisoNota}

\section{Gestión Integral del Portafolio}
\label{sec:prof-portafolio}
El portafolio reúne sus proyectos, su experiencia, su formación y sus habilidades. En
esta sección se documenta la gestión completa de cada bloque, paso a paso.

\subsection{Creación de un Nuevo Proyecto}
\label{subsec:prof-crear-proyecto}
La creación de un proyecto se realiza mediante un asistente de tres pasos: General,
Técnico y Media.

\subsubsection{Paso 1: Navegación al formulario de creación}
""")
A(bt(PROY, (1, 2)))
A(r"""
\subsubsection{Paso 2: Llenado de campos obligatorios (General y Técnico)}
""")
A(bt(PROY, (3, 24)))
A(r"""
\subsubsection{Paso 3: Carga de recursos multimedia y confirmación}
""")
A(bt(PROY, (25, 37)))
A(r"""
\subsection{Edición y Actualización de Proyectos Existentes}
\label{subsec:prof-editar-proyecto}
Una vez creado, el proyecto aparece en el listado de \campo{Proyectos y Evidencias},
donde puede consultarse, filtrarse y editarse.
""")
A(bt(PROY, (38, 49)))
A(r"""
\subsection{Eliminación o Depuración de Elementos del Portafolio}
\label{subsec:prof-eliminar-proyecto}
""")
A(bt(PROY, (50, 52)))
A(r"""
\begin{AvisoAdvertencia}
La eliminación de un proyecto es permanente. Asegúrese de no necesitar su información
antes de confirmar el borrado.
\end{AvisoAdvertencia}

\subsection{Registro de Experiencia Laboral}
\label{subsec:prof-experiencia}
El bloque \campo{Experiencia} permite documentar cada puesto de trabajo con sus fechas,
ubicación, tecnologías y evidencias visuales.
""")
A(bt(EXP))
A(r"""
\subsection{Registro de Formación Académica (Educación)}
\label{subsec:prof-educacion}
El bloque \campo{Educación} registra y muestra su formación y certificaciones.
""")
A(g.block_from_list(P + "/05_educacion", [c for _, c in EDU],
                    order=[f for f, _ in EDU]))
A(r"""
\subsection{Generación de Currículum con CV Studio}
\label{subsec:prof-cvstudio}
\campo{CV Studio} permite generar currículums profesionales a partir de plantillas en
formato LaTeX o Markdown, con apoyo de un asistente de inteligencia artificial, y
exportarlos o guardarlos en el perfil.
""")
A(g.block_from_list(P + "/06_cv-studio", CV))
A(r"""
\section{Mecanismos de Validación de Habilidades}
\label{sec:prof-habilidades}
El bloque \campo{Habilidades} permite declarar las competencias técnicas (hard skills)
y blandas (soft skills), asignarles un nivel y destacarlas para su validación pública
en la sección \campo{Top Skills}.

\subsection{Solicitud Formal de Validación Técnica (Hard Skills)}
\label{subsec:prof-hardskills}
""")
A(bt(HAB, (1, 7)))
A(r"""
\subsection{Monitoreo y Seguimiento del Estado de la Solicitud}
\label{subsec:prof-topskills}
Tras registrar una habilidad técnica puede editar su nivel, destacarla en
\campo{Top Skills}, reordenar las destacadas y filtrarlas por categoría.
""")
A(bt(HAB, (8, 19)))
A(r"""
\subsection{Registro de Habilidades Blandas (Soft Skills)}
\label{subsec:prof-softskills}
""")
A(bt(HAB, (20, 31)))
A(r"""
\section{Configuración y Privacidad del Perfil Público}
\label{sec:prof-configuracion}
Desde \campo{Configuración} se gestionan la identidad del perfil, la personalización de
la interfaz, la seguridad de la cuenta y la exportación o eliminación de datos.

\subsection{Identidad del Perfil}
\label{subsec:prof-identidad}
""")
A(bt(CFG, (1, 23)))
A(r"""
\subsection{Personalización de la Interfaz}
\label{subsec:prof-personalizacion}
""")
A(bt(CFG, (24, 27)))
A(r"""
\subsection{Seguridad de la Cuenta}
\label{subsec:prof-seguridad}
""")
A(bt(CFG, (28, 45)))
A(r"""
\subsection{Exportación de Datos y Zona de Peligro}
\label{subsec:prof-datos}
""")
A(bt(CFG, (46, 52)))
A(r"""
\begin{AvisoAdvertencia}
La eliminación de la cuenta es irreversible y borra todo su portafolio. El sistema exige
un código de verificación enviado a su correo antes de confirmar la acción.
\end{AvisoAdvertencia}

\section{Acceso desde Dispositivos Móviles (Diseño Adaptable)}
\label{sec:prof-responsive}
La plataforma cuenta con diseño adaptable (\textit{responsive}): todas las secciones del
perfil Profesional se reorganizan automáticamente para su uso cómodo en teléfonos y
tabletas. A continuación se muestran las vistas móviles más representativas.
""")
A(g.responsive_block(P + "/10_responsive", RESP))

out_path = os.path.join(g.ABS_ROOT, "sections", "cap03", "00_profesional.tex")
with open(out_path, "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT) + "\n")
print("written", out_path)
