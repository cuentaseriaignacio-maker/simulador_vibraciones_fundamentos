import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

st.set_page_config(
    page_title="Simulador de Vibraciones: Resonancia, Desfase y Amortiguamiento",
    layout="wide",
)

st.title(
    "🌀 Laboratorio de Vibraciones Mecánicas: Resonancia, Desfase y"
    " Transmisibilidad"
)
st.markdown("""
**Simulador Dinámico de 1 Grado de Libertad (1-DOF):** Explora cómo varían la **Amplitud de Vibración**, 
el **Ángulo de Desfase ($\phi$)** y la **Fuerza Transmitida a la Fundación** al cambiar la velocidad del motor ($r = \omega/\omega_n$) 
y la razón de amortiguamiento ($\zeta$).
""")

# --- BARRA LATERAL: PARÁMETROS DEL SISTEMA ---
st.sidebar.header("1. 🛠️️ Propiedades Mecánicas del Sistema")
m = st.sidebar.slider("Masa (m) [kg]", 1.0, 100.0, 10.0, step=1.0)
k = st.sidebar.slider(
    "Rigidez del Resorte (k) [N/m]", 100.0, 10000.0, 2000.0, step=100.0
)

# Amortiguamiento interactivo (zeta)
st.sidebar.markdown("---")
st.sidebar.header("2. 💧 Amortiguamiento (c / ζ)")
zeta = st.sidebar.slider(
    "Razón de Amortiguamiento (ζ)",
    0.01,
    0.80,
    0.10,
    step=0.01,
    help=(
        "ζ = c / c_crítico. Controla la altura del pico de resonancia y la"
        " fuerza transmitida."
    ),
)

# Cálculos de Parámetros Físicos
wn = np.sqrt(k / m)  # rad/s
fn = wn / (2 * np.pi)  # Hz
c_critico = 2 * np.sqrt(k * m)  # N*s/m
c = zeta * c_critico  # N*s/m
wd = wn * np.sqrt(max(0, 1 - zeta**2))  # Frecuencia amortiguada

# Excitatriz
st.sidebar.markdown("---")
st.sidebar.header("3. 🎛️ Velocidad del Motor (Excitación)")
F0 = st.sidebar.slider("Fuerza Armónica F0 [N]", 10.0, 500.0, 100.0, step=10.0)
freq_motor_hz = st.sidebar.slider(
    "Frecuencia Motor (f_motor) [Hz]",
    0.1,
    float(2.5 * fn),
    float(fn * 0.5),
    step=0.1,
)

w_motor = 2 * np.pi * freq_motor_hz
r = w_motor / wn  # Razón de frecuencias (r = w / wn)

# --- CÁLCULOS DINÁMICOS Y BODE ---
# Magnificación de Amplitud (M)
M = 1.0 / np.sqrt((1 - r**2) ** 2 + (2 * zeta * r) ** 2)
# Ángulo de Desfase en grados (phi)
phi_rad = np.arctan2(2 * zeta * r, 1 - r**2)
phi_deg = np.degrees(phi_rad)
if phi_deg < 0:
  phi_deg += 360  # Rango continuo 0-180 deg

# Transmisibilidad de Fuerza (TR)
TR = np.sqrt((1 + (2 * zeta * r) ** 2) / ((1 - r**2) ** 2 + (2 * zeta * r) ** 2))
F_transmitida = F0 * TR
X_amp = (F0 / k) * M  # Amplitud de desplazamiento en metros

# Factor Q (Calidad)
Q = 1.0 / (2 * zeta)

# METRICAS PRINCIPALES
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Frec. Natural (fn)", f"{fn:.2f} Hz", f"wn = {wn:.1f} rad/s")
c2.metric("Factor Q (Resonancia)", f"{Q:.1f} X", f"1 / (2ζ)")
c3.metric("Razón Frecuencias (r)", f"{r:.2f}", "r = f_motor / fn")
c4.metric("Ángulo Desfase (ϕ)", f"{phi_deg:.1f}°")
c5.metric("Fuerza Transmitida", f"{F_transmitida:.1f} N", f"TR = {TR:.2f}")

st.markdown("---")

# ==============================================================================
# MÓDULO 1: DIAGRAMAS DE BODE (MAGNIFICACIÓN Y DESFASE)
# ==============================================================================
st.subheader(
    "1. 📊 Curvas de Respuesta en Frecuencia (Bode): Magnificación M(r) y"
    " Desfase ϕ(r)"
)

r_vec = np.linspace(0.01, 2.5, 600)
M_vec = 1.0 / np.sqrt((1 - r_vec**2) ** 2 + (2 * zeta * r_vec) ** 2)
phi_vec = np.degrees(np.arctan2(2 * zeta * r_vec, 1 - r_vec**2))
phi_vec = np.where(phi_vec < 0, phi_vec + 360, phi_vec)
TR_vec = np.sqrt(
    (1 + (2 * zeta * r_vec) ** 2) / ((1 - r_vec**2) ** 2 + (2 * zeta * r_vec) ** 2)
)

fig_bode = make_subplots(
    rows=1,
    cols=2,
    subplot_titles=(
        "a) Factor de Magnificación M(r) vs Razón de Frecuencias",
        "b) Ángulo de Desfase ϕ(r) [Fuerza vs Desplazamiento]",
    ),
)

# Gráfico a) Magnificación
fig_bode.add_trace(
    go.Scatter(
        x=r_vec,
        y=M_vec,
        mode="lines",
        name="Magnificación M(r)",
        line=dict(color="#1f77b4", width=2.5),
    ),
    row=1,
    col=1,
)
fig_bode.add_trace(
    go.Scatter(
        x=[r],
        y=[M],
        mode="markers+text",
        name="Punto Actual",
        marker=dict(color="red", size=12, symbol="diamond"),
        text=[f"r={r:.2f}, M={M:.1f}"],
        textposition="top center",
    ),
    row=1,
    col=1,
)
fig_bode.add_vline(
    x=1.0,
    line_dash="dash",
    line_color="orange",
    annotation_text="Resonancia (r=1.0)",
    row=1,
    col=1,
)

# Gráfico b) Desfase
fig_bode.add_trace(
    go.Scatter(
        x=r_vec,
        y=phi_vec,
        mode="lines",
        name="Desfase ϕ(r)",
        line=dict(color="#2ca02c", width=2.5),
    ),
    row=1,
    col=2,
)
fig_bode.add_trace(
    go.Scatter(
        x=[r],
        y=[phi_deg],
        mode="markers+text",
        name="Desfase Actual",
        marker=dict(color="red", size=12, symbol="diamond"),
        text=[f"ϕ={phi_deg:.1f}°"],
        textposition="top center",
    ),
    row=1,
    col=2,
)
fig_bode.add_hline(
    y=90.0,
    line_dash="dot",
    line_color="gray",
    annotation_text="90° en Resonancia",
    row=1,
    col=2,
)
fig_bode.add_vline(
    x=1.0, line_dash="dash", line_color="orange", row=1, col=2
)

fig_bode.update_layout(template="plotly_white", height=360)
fig_bode.update_xaxes(title_text="Razón de Frecuencias r = ω / ωn")
fig_bode.update_yaxes(title_text="Magnificación M = X / δ_st", row=1, col=1)
fig_bode.update_yaxes(title_text="Ángulo de Desfase ϕ (°)", row=1, col=2)
st.plotly_chart(fig_bode, use_container_width=True)

st.markdown("---")

# ==============================================================================
# MÓDULO 2: TRANSMISIBILIDAD DE FUERZA A LA FUNDACIÓN
# ==============================================================================
col_tr1, col_tr2 = st.columns([1.2, 1.0])

with col_tr1:
  st.subheader("2. 🛡️ Curva de Transmisibilidad de Fuerza (TR)")
  st.markdown("""
    La **Transmisibilidad ($TR$)** mide la fracción de fuerza dinámica que llega a la estructura o fundación.
    * **Si $r < \sqrt{2} \approx 1.41$:** La fuerza se amplifica ($TR > 1$). Aumentar el amortiguamiento ($\zeta$) **ayuda a reducir la fuerza**.
    * **Si $r > \sqrt{2}$ (Zona de Aislamiento):** La fuerza se atenúa ($TR < 1$).
    """)

  fig_tr = go.Figure()
  fig_tr.add_trace(
      go.Scatter(
          x=r_vec,
          y=TR_vec,
          mode="lines",
          name="Transmisibilidad TR(r)",
          line=dict(color="#d62728", width=2.5),
      )
  )
  fig_tr.add_trace(
      go.Scatter(
          x=[r],
          y=[TR],
          mode="markers+text",
          name="TR Actual",
          marker=dict(color="black", size=12),
          text=[f"TR = {TR:.2f}"],
          textposition="top center",
      )
  )
  fig_tr.add_vline(
      x=np.sqrt(2),
      line_dash="dash",
      line_color="purple",
      annotation_text="r = √2 (Aislamiento TR < 1)",
  )
  fig_tr.add_hline(y=1.0, line_dash="dot", line_color="gray")
  fig_tr.update_layout(
      xaxis_title="Razón de Frecuencias (r)",
      yaxis_title="Transmisibilidad TR = F_trans / F0",
      template="plotly_white",
      height=340,
  )
  st.plotly_chart(fig_tr, use_container_width=True)

with col_tr2:
  st.subheader("💡 Tres Regiones Clave de la Dinámica")
  st.info(f"""
    **1. Región de Rigidez ($r \ll 1$):**
    * El movimiento está controlado por el resorte ($k$).
    * El desplazamiento está **en fase** con la fuerza ($\phi \approx 0^\circ$).
    
    **2. Región de Amortiguamiento ($r \approx 1.0$ — RESONANCIA):**
    * El pico de vibración depende **exclusivamente de $\zeta$**.
    * La masa se mueve **$90^\circ$ retrasada** respecto a la fuerza excitatriz.
    * Con $\zeta = {zeta:.2f}$, la vibración se magnifica **{M:.1f} veces**.
    
    **3. Región de Inercia ($r \gg 1$):**
    * La masa ($m$) domina la respuesta.
    * Movimiento en **oposición de fase ($\phi \approx 180^\circ$)**.
    * A partir de $r > \sqrt{{2}}$, el sistema entra en **aislamiento de vibraciones**.
    """)

st.markdown("---")

# ==============================================================================
# MÓDULO 3: ANIMACIÓN FÍSICA Y ONDAS DE TIEMPO
# ==============================================================================
st.subheader("3. 🏗️️ Animación Física del Resorte-Amortiguador y Onda Temporal")

t_sim = np.linspace(0, 4.0 / (freq_motor_hz if freq_motor_hz > 0 else 1.0), 300)
x_t = X_amp * np.cos(w_motor * t_sim - phi_rad)
fuerza_t = F0 * np.cos(w_motor * t_sim)

instante_idx = st.slider(
    "Pasos de Tiempo (Desplaza para observar el movimiento del resorte)",
    0,
    len(t_sim) - 1,
    50,
)
t_act = t_sim[instante_idx]
pos_x = x_t[instante_idx]
fuerza_act = fuerza_t[instante_idx]

col_a1, col_a2 = st.columns([1.0, 1.5])

with col_a1:
  fig_anim = go.Figure()
  # Base Techo
  fig_anim.add_shape(
      type="rect",
      x0=-0.6,
      y0=0.8,
      x1=0.6,
      y1=0.85,
      fillcolor="gray",
      line=dict(color="black"),
  )

  # Resorte zig-zag (Azul)
  y_spring = np.linspace(0.8, pos_x + 0.2, 15)
  x_spring = -0.15 + 0.08 * np.sin(np.pi * np.arange(15))
  fig_anim.add_trace(
      go.Scatter(
          x=x_spring,
          y=y_spring,
          mode="lines",
          line=dict(color="blue", width=2.5),
          name="Resorte (k)",
      )
  )

  # Amortiguador (Naranja)
  fig_anim.add_trace(
      go.Scatter(
          x=[0.15, 0.15],
          y=[0.8, pos_x + 0.2],
          mode="lines",
          line=dict(color="orange", width=4),
          name="Amortiguador (c)",
      )
  )

  # Bloque de Masa (m)
  color_bloque = "crimson" if abs(r - 1.0) < 0.15 else "#1f77b4"
  fig_anim.add_shape(
      type="rect",
      x0=-0.4,
      y0=pos_x - 0.2,
      x1=0.4,
      y1=pos_x + 0.2,
      fillcolor=color_bloque,
      line=dict(color="black"),
  )
  fig_anim.add_annotation(
      x=0,
      y=pos_x,
      text=f"<b>Masa m</b><br>{m:.0f} kg",
      showarrow=False,
      font=dict(color="white", size=12),
  )

  fig_anim.update_layout(
      title=f"Posición t = {t_act:.3f} s | x = {pos_x*1000:.1f} mm",
      xaxis=dict(range=[-1, 1], visible=False),
      yaxis=dict(range=[-1.2, 1.0], title="Desplazamiento Vertical (m)"),
      template="plotly_white",
      height=380,
  )
  st.plotly_chart(fig_anim, use_container_width=True)

with col_a2:
  fig_waves = go.Figure()
  fig_waves.add_trace(
      go.Scatter(
          x=t_sim,
          y=fuerza_t / np.max(np.abs(fuerza_t)),
          mode="lines",
          name="Fuerza F(t) [Normalizada]",
          line=dict(color="gray", width=1.5, dash="dash"),
      )
  )
  fig_waves.add_trace(
      go.Scatter(
          x=t_sim,
          y=x_t / np.max(np.abs(x_t)) if np.max(np.abs(x_t)) > 0 else x_t,
          mode="lines",
          name=f"Desplazamiento x(t) [Desfase = {phi_deg:.1f}°]",
          line=dict(color="crimson", width=2.5),
      )
  )
  fig_waves.add_vline(
      x=t_act, line_width=1.5, line_color="black", line_dash="dot"
  )

  fig_waves.update_layout(
      title="Comparación Temporal: Fuerza Excitatriz vs Respuesta de la Masa",
      xaxis_title="Tiempo (s)",
      yaxis_title="Amplitud Normalizada",
      template="plotly_white",
      height=380,
  )
  st.plotly_chart(fig_waves, use_container_width=True)
