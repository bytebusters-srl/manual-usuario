#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera sections/cap05/00_administrador.tex (Perfil Administrador)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import genlib as g

AD = "ethoshub-administrador"
MET = (AD + "/01_metricas-globales", "administrador_metricas_globales_",
       AD + "/01_metricas-globales/descripcion imagenes-administrador-metricas-globales.txt")

# --- 5.1 Backoffice / extras (6) ---------------------------------------------
EXTRAS = [
 "Panel de administración (Métricas Globales): es la pantalla de inicio del backoffice, con la barra de navegación superior (Métricas Globales, Gestión de Perfiles, Moderación, Skills y Email), las tarjetas de indicadores y los gráficos de crecimiento y distribución por rol.",
 "En la esquina superior derecha, el icono de campana muestra las notificaciones del sistema y, junto a él, el menú de la cuenta de administrador.",
 "El backoffice también dispone de tema oscuro; la información y los gráficos se mantienen idénticos con la paleta oscura.",
 "Al pulsar el avatar de la cuenta se despliega el menú de usuario del administrador.",
 "El botón de la esquina superior derecha permite cerrar la sesión de administrador de forma segura.",
 "Pantalla de inicio de sesión de la plataforma, desde la que el administrador accede al backoffice con sus credenciales.",
]

# --- 5.2 Gestión de perfiles / usuarios (25) ---------------------------------
USUARIOS = [
 "Para abrir la gestión de cuentas, en la barra superior haga clic en \\boton{Gestión de Perfiles}.",
 "Vista de \\campo{Gestión de Perfiles}: una tabla con todas las cuentas y sus columnas de perfil, rol, estado, habilidades, proyectos y fecha de registro.",
 "El botón \\boton{Registrar usuario} (arriba a la derecha) permite dar de alta una cuenta nueva en la plataforma.",
 "El botón \\boton{Registrar admin} crea una cuenta con privilegios de administrador.",
 "El filtro \\campo{Todos los roles} permite acotar el listado por tipo de perfil.",
 "Al desplegar \\campo{Todos los roles} se muestran las opciones: Profesional, Reclutador y Administrador.",
 "Seleccione un rol en el desplegable para filtrar la tabla por ese tipo de perfil.",
 "La tabla se actualiza y muestra únicamente las cuentas del rol elegido.",
 "El desplegable de rol permite alternar el criterio de filtrado en cualquier momento.",
 "Resultado del filtrado por rol aplicado a la tabla de perfiles.",
 "Despliegue del filtro para seleccionar otro rol disponible.",
 "La tabla refleja el nuevo rol seleccionado en el filtro.",
 "El filtro \\campo{Todos los estados} permite acotar las cuentas por su situación.",
 "Al desplegar \\campo{Todos los estados} se muestran los estados disponibles (por ejemplo, Activo y Suspendido).",
 "Seleccione un estado para filtrar las cuentas según su situación actual.",
 "La tabla muestra las cuentas que coinciden con el estado elegido.",
 "Los filtros de rol y estado pueden combinarse para refinar la búsqueda de cuentas.",
 "Resultado de combinar los filtros de rol y estado sobre el listado.",
 "El desplegable de estado permite alternar entre las distintas situaciones de cuenta.",
 "Cuando ningún registro coincide con los filtros aplicados, se muestra el mensaje \\campo{Sin resultados}.",
 "El campo \\campo{Buscar usuario} localiza una cuenta por su nombre o correo electrónico.",
 "Los controles de paginación, en la parte inferior, permiten recorrer el listado cuando hay muchas cuentas.",
 "Página siguiente del listado de perfiles.",
 "Avance entre las páginas de resultados mediante las flechas de paginación.",
 "Vista completa de la tabla de \\campo{Gestión de Perfiles}; cada fila incluye, además, las acciones de auditar la cuenta, suspenderla o modificar su rol.",
]

# --- 5.3.1 Moderación (42) ---------------------------------------------------
MODERACION = [
 "Para abrir la moderación, en la barra superior haga clic en \\boton{Moderación}.",
 "Vista de \\campo{Moderación}: listado de perfiles y contenidos reportados, con etiquetas de estado y un indicador de alerta por fila.",
 "El filtro superior derecho permite acotar los elementos a moderar.",
 "Al desplegar el filtro se muestran las opciones para clasificar los reportes.",
 "Seleccione un criterio del filtro para mostrar solo los elementos correspondientes.",
 "El listado se actualiza según el criterio de filtrado elegido.",
 "El filtro permite alternar entre los distintos estados de los reportes.",
 "Resultado del filtrado aplicado al listado de moderación.",
 "Despliegue del filtro para seleccionar otro estado de reporte.",
 "El listado muestra los elementos que coinciden con el filtro seleccionado.",
 "Puede combinar criterios de filtrado para localizar reportes concretos.",
 "Al desplegar el segundo filtro se muestran las categorías de contenido reportable.",
 "Seleccione una categoría para acotar los reportes por tipo de contenido.",
 "El listado refleja la categoría de contenido seleccionada.",
 "El filtro de categoría permite alternar entre los distintos tipos de contenido.",
 "Resultado del filtrado por categoría sobre el listado de moderación.",
 "Combine los filtros de estado y categoría para una revisión más precisa.",
 "Cuando ningún reporte coincide con los filtros, se muestra el mensaje de listado vacío.",
 "El campo de búsqueda permite localizar un reporte por el nombre del perfil afectado.",
 "Pulse el enlace de acción de una fila (\\boton{Inspeccionar}) para revisar el perfil reportado en detalle.",
 "Se abre la ventana de \\campo{Inspección} del perfil, organizada en pestañas; la primera muestra los datos generales.",
 "La segunda pestaña presenta los proyectos del perfil inspeccionado.",
 "Otra pestaña muestra las habilidades declaradas por el perfil.",
 "Desde la ventana de inspección se accede a las acciones de moderación disponibles.",
 "Cada pestaña de inspección facilita la revisión de un aspecto distinto del perfil reportado.",
 "En la pestaña de reportes se listan las incidencias asociadas al perfil, resaltadas en rojo.",
 "Cada reporte dispone de un botón \\boton{Resolver} para gestionarlo individualmente.",
 "La ventana permite revisar el detalle de cada reporte antes de tomar una decisión.",
 "El listado de reportes del perfil se mantiene visible mientras se gestionan las incidencias.",
 "La acción de moderación correspondiente se confirma desde la propia ventana de inspección.",
 "La pestaña de reportes resalta los elementos pendientes de revisión.",
 "El botón \\boton{Resolver} marca el reporte como atendido.",
 "Las incidencias resueltas dejan de aparecer como pendientes en la ventana.",
 "El botón \\boton{X} (esquina superior derecha) cierra la ventana de inspección.",
 "De vuelta en el listado, los controles de fila permiten aplicar acciones rápidas de moderación.",
 "Al elegir suspender o silenciar un perfil, el sistema solicita confirmación mediante una ventana \\campo{Silenciar perfil}.",
 "La ventana de confirmación ofrece los botones \\boton{Cancelar} y la acción de moderación correspondiente.",
 "El botón \\boton{X} de la ventana de confirmación cancela la acción sin aplicarla.",
 "Tras aplicar una acción, el listado de moderación se actualiza; la paginación permite recorrer los demás reportes.",
 "El listado resalta la fila sobre la que se ha actuado recientemente.",
 "Los controles de paginación permiten avanzar por el resto de los reportes.",
 "Vista final del listado de moderación con los reportes pendientes y atendidos.",
]

# --- 5.3.2 Skills (29) -------------------------------------------------------
SKILLS = [
 "Para abrir el repositorio de habilidades, en la barra superior haga clic en \\boton{Skills}.",
 "Vista de \\campo{Normalización de Skills}: tabla del repositorio global con el nombre de la habilidad, su categoría, el número de usos y su estado.",
 "Las tarjetas superiores resumen el total de habilidades y su distribución por estado.",
 "El botón \\boton{Agregar skill} (arriba a la derecha) permite registrar una nueva habilidad global.",
 "Al pulsar \\boton{Agregar skill} se abre la ventana de alta de una habilidad.",
 "En la ventana de alta, el primer campo solicita el \\campo{Nombre} de la habilidad.",
 "Introduzca el nombre de la nueva habilidad en el campo correspondiente.",
 "El campo \\campo{Categoría} se elige mediante un desplegable con las categorías disponibles.",
 "Seleccione la categoría que mejor clasifique la habilidad.",
 "Un interruptor permite marcar la habilidad como oficial o activa antes de guardarla.",
 "Pulse \\boton{Agregar} para registrar la habilidad en el repositorio global.",
 "El campo de búsqueda permite localizar rápidamente una habilidad por su nombre.",
 "El filtro superior permite acotar el repositorio por categoría.",
 "Al desplegar el filtro de categoría se muestran todas las categorías disponibles.",
 "Seleccione una categoría para mostrar solo las habilidades correspondientes.",
 "El filtro de estado permite acotar por situación de la habilidad (activa, pendiente, etc.).",
 "Al desplegar el filtro de estado se muestran las situaciones posibles.",
 "El listado se actualiza según el estado seleccionado en el filtro.",
 "Las casillas de selección permiten elegir varias habilidades para una acción conjunta.",
 "El estado de cada habilidad se indica con una etiqueta de color en su fila.",
 "El enlace de acción de la fila (\\boton{Editar}) permite modificar la habilidad seleccionada.",
 "También es posible fusionar habilidades duplicadas desde las acciones de la fila.",
 "Al pulsar \\boton{Editar} se abre la ventana de edición de la habilidad.",
 "La ventana de edición permite modificar el nombre de la habilidad.",
 "Asimismo, permite cambiar la categoría asignada a la habilidad.",
 "Un interruptor permite ajustar el estado oficial o activo de la habilidad.",
 "Pulse \\boton{Guardar} para aplicar los cambios a la habilidad.",
 "El botón \\boton{X} cierra la ventana de edición sin guardar.",
 "Vista del repositorio con los controles de paginación para recorrer todas las habilidades.",
]

# --- 5.5 Email (14) ----------------------------------------------------------
EMAIL = [
 "Para abrir el envío de comunicaciones, en la barra superior haga clic en \\boton{Email}.",
 "Vista del compositor de \\campo{Email}: incluye el campo de destinatarios, el asunto, las pestañas Redactar/Plantillas y el editor de contenido.",
 "El campo \\campo{Destinatarios} permite escribir o buscar a las personas que recibirán el correo.",
 "Al escribir en el campo de destinatarios, el sistema sugiere cuentas coincidentes para seleccionarlas.",
 "El campo \\campo{Asunto} define el título del correo que se enviará.",
 "Las pestañas \\boton{Redactar} y \\boton{Plantillas} alternan entre la escritura libre y el uso de plantillas predefinidas.",
 "En la pestaña \\boton{Redactar}, el editor permite escribir y dar formato al cuerpo del mensaje.",
 "La pestaña \\boton{Plantillas} ofrece plantillas de correo prediseñadas.",
 "Al elegir una plantilla se muestra su previsualización en el cuerpo del mensaje.",
 "El botón \\boton{Enviar} (arriba a la derecha) inicia el envío del correo.",
 "Antes de enviar, el sistema solicita confirmación mediante la ventana \\campo{Enviar correo}.",
 "La ventana de confirmación ofrece los botones \\boton{Cancelar} y \\boton{Enviar}.",
 "El botón \\boton{Cancelar} (o \\boton{X}) cierra la confirmación sin enviar el correo.",
 "Tras el envío, el compositor se restablece y queda listo para una nueva comunicación.",
]

# --- 5.6 Responsive admin (9) ------------------------------------------------
RESP = [
 ("administrador_responsive_metricas_globales.jpg", "Métricas Globales en vista móvil."),
 ("administrador_responsive_metricas_globales_tendencias.jpg", "Tendencias de Métricas Globales en móvil."),
 ("administrador_responsive_metricas_globales_top_skills.jpg", "Top Skills de Métricas Globales en móvil."),
 ("administrador_responsive_metricas_globales_sistemas_logs.jpg", "Sistema y Logs de Métricas Globales en móvil."),
 ("administrador_responsive_gestion_perfiles.jpg", "Gestión de Perfiles en vista móvil."),
 ("administrador_responsive_moderacion.jpg", "Moderación en vista móvil."),
 ("administrador_responsive_skills.jpg", "Repositorio de Skills en vista móvil."),
 ("administrador_responsive_skills_agregar.jpg", "Alta de una skill en vista móvil."),
 ("administrador_responsive_email.jpg", "Compositor de Email en vista móvil."),
]

def order_from(prefix_files):
    return prefix_files

OUT = []; A = OUT.append
A(r"""% =============================================================================
% CAPÍTULO 5 — GUÍA OPERATIVA: PERFIL ADMINISTRADOR  (generado por tools/gen_ch5.py)
% =============================================================================
\chapter{Guía Operativa: Perfil Administrador}
\label{ch:administrador}
\resumenCapitulo{Este capítulo guía a la persona usuaria con perfil Administrador en el
uso del panel de administración (backoffice): la gestión de cuentas y roles, la
moderación de contenido, la administración del repositorio global de habilidades, el
monitoreo de métricas del sistema, el envío de comunicaciones y el acceso móvil.}

\section{Visión General del Panel de Administración (Backoffice)}
\label{sec:adm-backoffice}
El \textit{backoffice} es el espacio de trabajo del Administrador. Su barra de
navegación superior da acceso a las cinco áreas de gestión: \campo{Métricas Globales},
\campo{Gestión de Perfiles}, \campo{Moderación}, \campo{Skills} y \campo{Email}.
""")
A(g.block_from_list(AD + "/07_extras", EXTRAS))
A(r"""
\section{Control y Gestión de Perfiles del Sistema}
\label{sec:adm-perfiles}
La sección \campo{Gestión de Perfiles} centraliza la administración de todas las cuentas
de la plataforma mediante una tabla con filtros, búsqueda y acciones por fila.

\subsection{Auditoría, Suspensión y Alta de Cuentas}
\label{subsec:adm-altas}
""")
A(g.block_from_list(AD + "/02_gestion-usuarios", USUARIOS[:12],
                    order=g.list_images(AD + "/02_gestion-usuarios")[:12]))
A(r"""
\subsection{Modificación Directa de Roles y Permisos Especiales}
\label{subsec:adm-roles}
La columna \campo{Rol} y el filtro de roles permiten identificar y modificar el tipo de
cada cuenta; las acciones por fila habilitan el cambio de rol y de permisos.
""")
A(g.block_from_list(AD + "/02_gestion-usuarios", USUARIOS[12:],
                    order=g.list_images(AD + "/02_gestion-usuarios")[12:]))
A(r"""
\section{Moderación de Contenido y Validaciones}
\label{sec:adm-moderacion}
El Administrador revisa los reportes de contenido, inspecciona los perfiles afectados y
aplica acciones correctivas, además de administrar el repositorio global de habilidades.

\subsection{Revisión de Reportes y Alertas de Contenido}
\label{subsec:adm-reportes}
""")
A(g.block_from_list(AD + "/03_moderacion", MODERACION))
A(r"""
\subsection{Gestión del Repositorio de Habilidades Globales}
\label{subsec:adm-skills}
La sección \campo{Skills} (Normalización de Skills) administra el catálogo global de
habilidades que las personas profesionales pueden añadir a su portafolio.
""")
A(g.block_from_list(AD + "/04_skills", SKILLS))
A(r"""
\section{Monitoreo, Métricas y Configuración Global del Sistema}
\label{sec:adm-metricas}
La sección \campo{Métricas Globales} ofrece el monitoreo integral de la plataforma:
indicadores de uso, tendencias, top de habilidades, estado del sistema y registros
(logs), con rangos temporales configurables.
""")
A(g.block_from_txt(MET[0], MET[1], MET[2]))
A(r"""
\section{Gestión de Comunicaciones por Correo (Email)}
\label{sec:adm-email}
La sección \campo{Email} permite al Administrador redactar y enviar comunicaciones a las
personas usuarias, ya sea con texto libre o a partir de plantillas predefinidas.
""")
A(g.block_from_list(AD + "/05_email", EMAIL))
A(r"""
\section{Acceso desde Dispositivos Móviles (Diseño Adaptable)}
\label{sec:adm-responsive}
El panel de administración también se adapta a teléfonos y tabletas. A continuación se
muestran las vistas móviles más representativas del backoffice.
""")
A(g.responsive_block(AD + "/responsive", RESP))

out_path = os.path.join(g.ABS_ROOT, "sections", "cap05", "00_administrador.tex")
with open(out_path, "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT) + "\n")
print("written", out_path)
