# simulador_vibraciones_fundamentos
Simulador de comportamiento de 1 GDL estimulado por una fuerza rotatoria
# 🌀 Simulador Didáctico de Vibraciones Mecánicas y Resonancia (1-DOF)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red.svg)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Simulador interactivo en **Python**, **Streamlit** y **Plotly** desarrollado para la enseñanza de la dinámica de sistemas mecánicos de **Un Grado de Libertad (1-DOF)**. 

La herramienta permite analizar en tiempo real los cuatro regímenes de movimiento fundamentales, la respuesta en frecuencia (curva de magnificación), el ángulo de desfase (\\(\phi\\)) y la animación física del conjunto masa-resorte-amortiguador.

---

## 🚀 Acceso a la Aplicación Web

Puedes utilizar el simulador directamente desde tu navegador sin instalar nada:
👉 **[Abrir Simulador en Streamlit Cloud](https://tu-usuario.streamlit.app)** *(reemplaza esta URL con el enlace de tu app)*

---

## 🕹️ Los 4 Regímenes de Movimiento Simulados

El usuario puede seleccionar desde el menú lateral el comportamiento que desea analizar:

1. **Movimiento Armónico Simple (\\(c = 0\\)):**
   - Oscilación perpetua no amortiguada a la frecuencia natural \\(f_n = \frac{1}{2\pi}\sqrt{\frac{k}{m}}\\).
   - Conservación de energía mecánica y amplitud constante.

2. **Movimiento Libre Amortiguado (\\(c > 0\\)):**
   - Decaimiento natural de la oscilación en el tiempo.
   - Visualización de la envolvente exponencial de amortiguamiento \\(e^{-\zeta \omega_n t}\\).

3. **Movimiento Forzado por Impacto Único (Golpe de Martillo / Bump Test):**
   - Simulación de la respuesta al impulso usada en mantenimiento predictivo para determinar la frecuencia natural \\(f_n\\) de estructuras e inactivas.

4. **Movimiento Forzado Continuo por Motor (Resonancia):**
   - Análisis de la velocidad del motor (\\(r = \omega/\omega_n\\)).
   - Búsqueda del pico de magnificación dinámica (\\(M\\)), ángulo de desfase de \\(90^\circ\\) en resonancia y curva de respuesta en frecuencia.

---

## 📐 Fundamentos Físicos y Ecuaciones

El sistema se rige por la ecuación diferencial de segundo orden:

\\[m \ddot{x}(t) + c \dot{x}(t) + k x(t) = F(t)\\]

### Ecuaciones Principales

* **Frecuencia Natural (\\(\omega_n\\)):**
  \\[\omega_n = \sqrt{\frac{k}{m}} \quad [\text{rad/s}], \qquad f_n = \frac{\omega_n}{2\pi} \quad [\text{Hz}]\\]

* **Razón de Amortiguamiento (\\(\zeta\\)):**
  \\[\zeta = \frac{c}{c_{\text{crítico}}} = \frac{c}{2\sqrt{k m}}\\]

* **Factor de Magnificación Dinámica (\\(M\\)):**
  \\[M(r, \zeta) = \frac{X}{\delta_{st}} = \frac{1}{\sqrt{(1 - r^2)^2 + (2\zeta r)^2}}\\]
  *donde \\(r = \frac{\omega}{\omega_n}\\) es la razón de frecuencias entre el motor (\\(\omega\\)) y el sistema (\\(\omega_n\\)).*

* **Ángulo de Desfase (\\(\phi\\)):**
  \\[\phi(r, \zeta) = \arctan\left(\frac{2\zeta r}{1 - r^2}\right) \quad [\text{grados}]\\]

* **Factor de Calidad en Resonancia (\\(Q\\)):**
  \\[Q \approx \frac{1}{2\zeta}\\]

---

## 🏗️ Animación Interactiva

El simulador genera fotogramas en tiempo real para visualizar el movimiento del resorte y la masa mediante controles integrados de **`▶ Reproducir Animación`** y **`⏸ Pausa`**, permitiendo observar:
- La velocidad de oscilación de la masa.
- La compresión/extensión del resorte y la acción del amortiguador.
- El cambio de color del bloque en la zona de resonancia (\\(r \approx 1.0\\)).

---

## 🛠️ Ejecución Local en PC

Para ejecutar esta aplicación localmente en tu computadora:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/mi-simulador-vibraciones.git
   cd mi-simulador-vibraciones
