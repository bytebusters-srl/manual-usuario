#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera sections/cap04/00_reclutador.tex (Perfil Reclutador)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import genlib as g

R = "ethoshub-reclutador"
DASH = (R + "/01_dashboard", "DashboardReclutador", R + "/01_dashboard/Dashboard.txt")
BUSCAR = (R + "/02_buscar-talento", "BuscarTalento", R + "/02_buscar-talento/BuscarTalento.txt")
RANK = (R + "/03_rankings", "RankingReclutador", R + "/03_rankings/RankingReclutador.txt")
PIPE = (R + "/04_pipelines", "PipelinesReclutador", R + "/04_pipelines/PipelinesReclutador.txt")
CHAT = (R + "/05_chat", "ChatReclutador", R + "/05_chat/ChatReclutador.txt")
CFG = (R + "/06_configuracion", "configuracion_reclutador_", R + "/06_configuracion/Configuracion Reclutador.txt")

RESP = [
 ("reclutador_responsive_dashboard.jpg", "Dashboard del reclutador en vista móvil."),
 ("reclutador_responsive_dashboard_graficas.jpg", "Gráficas del dashboard en vista móvil."),
 ("reclutador_responsive_buscar_talento.jpg", "Buscar talento en vista móvil."),
 ("reclutador_responsive_rankings.jpg", "Rankings en vista móvil."),
 ("reclutador_responsive_pipelines.jpg", "Pipelines en vista móvil."),
 ("reclutador_responsive_chat_reclutador.jpg", "Bandeja de chat en vista móvil."),
 ("reclutador_responsive_chat_iniciado_reclutador.jpg", "Conversación iniciada en vista móvil."),
]

def bt(spec, rng=None):
    return g.block_from_txt(spec[0], spec[1], spec[2], rng)

OUT = []; A = OUT.append
A(r"""% =============================================================================
% CAPÍTULO 4 — GUÍA OPERATIVA: PERFIL RECLUTADOR  (generado por tools/gen_ch4.py)
% =============================================================================
\chapter{Guía Operativa: Perfil Reclutador}
\label{ch:reclutador}
\resumenCapitulo{Este capítulo guía a la persona usuaria con perfil Reclutador en el
uso del panel de reclutamiento: la búsqueda inteligente y filtrada de talento, la
revisión y evaluación de portafolios, la gestión del pipeline de selección, la
comunicación directa con los candidatos y la configuración de su cuenta.}

\section{Visión General del Panel de Reclutamiento}
\label{sec:rec-dashboard}
Al iniciar sesión como Reclutador accederá al \campo{Dashboard}, que reúne los
indicadores clave de su actividad (perfiles vistos, guardados, chats y contrataciones),
un resumen automático de desempeño y gráficos de mercado. Desde la barra superior se
navega a las secciones \campo{Buscar Talento}, \campo{Rankings}, \campo{Pipelines} y
\campo{Chat}.
""")
A(bt(DASH))
A(r"""
\section{Motores de Búsqueda de Talento}
\label{sec:rec-busqueda}
EthosHub ofrece dos mecanismos complementarios para localizar talento: la búsqueda
inteligente en lenguaje natural (asistida por IA) y los filtros avanzados por criterios
técnicos.

\subsection{Aplicación de Filtros Avanzados y Criterios Técnicos}
\label{subsec:rec-filtros}
""")
A(bt(BUSCAR, (1, 29)))
A(r"""
\subsection{Almacenamiento de Perfiles Favoritos y Listas de Seguimiento}
\label{subsec:rec-favoritos}
Tras localizar un perfil de interés puede revisarlo en detalle, guardarlo en su
\textit{pipeline} y abrir un canal de contacto directo.
""")
A(bt(BUSCAR, (30, 35)))
A(r"""
\section{Evaluación y Revisión de Portafolios}
\label{sec:rec-evaluacion}
La evaluación del talento combina la inspección de cada portafolio dentro del pipeline
de selección y la consulta de los rankings de competencia.

\subsection{Inspección de Proyectos y Evidencias Técnicas (Pipeline)}
\label{subsec:rec-pipeline}
El \textit{pipeline} organiza a los candidatos en columnas (Guardados, Revisión,
Entrevista, Oferta y Contratado) y permite compararlos técnicamente y obtener un
veredicto asistido por IA.
""")
A(bt(PIPE))
A(r"""
\subsection{Verificación de Sellos de Validación e Historial (Rankings)}
\label{subsec:rec-rankings}
La sección \campo{Rankings} clasifica el talento por competencia y permite filtrar por
área técnica, así como conocer el porqué de cada posición.
""")
A(bt(RANK))
A(r"""
\section{Gestión de Canales de Contacto Directo}
\label{sec:rec-chat}
La sección \campo{Chat} centraliza la comunicación con los candidatos, con soporte para
mensajes de texto, archivos adjuntos, notas de voz, fotografías, vídeo y emojis.
""")
A(bt(CHAT))
A(r"""
\section{Configuración de la Cuenta del Reclutador}
\label{sec:rec-config}
Desde \campo{Configuración} (icono de engranaje) se gestionan la identidad empresarial,
la personalización de la interfaz, la seguridad de la cuenta y la exportación o
eliminación de datos.

\subsection{Identidad Empresarial}
\label{subsec:rec-identidad}
""")
A(bt(CFG, (1, 21)))
A(r"""
\subsection{Personalización de la Interfaz}
\label{subsec:rec-personalizacion}
""")
A(bt(CFG, (22, 25)))
A(r"""
\subsection{Seguridad de la Cuenta}
\label{subsec:rec-seguridad}
""")
A(bt(CFG, (26, 41)))
A(r"""
\subsection{Exportación de Datos y Zona de Peligro}
\label{subsec:rec-datos}
""")
A(bt(CFG, (42, 50)))
A(r"""
\begin{AvisoAdvertencia}
La eliminación de la cuenta es irreversible. El sistema exige un código de verificación
enviado a su correo antes de confirmar la acción.
\end{AvisoAdvertencia}

\section{Acceso desde Dispositivos Móviles (Diseño Adaptable)}
\label{sec:rec-responsive}
El panel de reclutamiento también se adapta a teléfonos y tabletas. A continuación se
muestran las vistas móviles más representativas.
""")
A(g.responsive_block(R + "/07_responsive", RESP))

out_path = os.path.join(g.ABS_ROOT, "sections", "cap04", "00_reclutador.tex")
with open(out_path, "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT) + "\n")
print("written", out_path)
