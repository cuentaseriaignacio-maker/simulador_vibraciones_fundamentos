# simulador_vibraciones_fundamentos
Simulador de comportamiento de 1 GDL estimulado por una fuerza rotatoria
# 🌀 Laboratorio Virtual de Vibraciones Mecánicas y Resonancia (1-DOF)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red.svg)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Un simulador dinámico e interactivo desarrollado en **Python** y **Streamlit** diseñado para la enseñanza universitaria y técnica del comportamiento de sistemas mecánicos de **Un Grado de Libertad (1-DOF)** sometidos a excitación armónica (motores de velocidad variable) e impactos transitorios (Bump Test).

---

## 🚀 Acceso en Vivo (Web App)

Puedes ejecutar la aplicación directamente en tu navegador sin instalar nada:
👉 **[Acceder al Simulador Online en Streamlit Cloud](https://tu-usuario-o-app.streamlit.app)** *(Reemplazar con tu enlace)*

---

## 🎯 Objetivos Pedagógicos y de Ingeniería

* **Visualizar la Resonancia:** Comprender la amplificación drástica de la vibración cuando la frecuencia del motor (\\(\omega\\)) coincide con la frecuencia natural (\\(\omega_n\\)).
* **Analizar el Ángulo de Desfase (\\(\phi\\)):** Observar la transición continua de fase desde \\(0^\circ\\) (baja velocidad), pasando por \\(90^\circ\\) en resonancia, hasta \\(180^\circ\\) a altas velocidades.
* **Evaluar el Amortiguamiento (\\(\zeta\\)):** Analizar el efecto del coeficiente de amortiguamiento en el factor de calidad (\\(Q \approx 1/2\zeta\\)) y en la reducción de fuerzas destructivas.
* **Estudiar la Transmisibilidad de Fuerza (\\(TR\\)):** Identificar la zona crítica de amplificación (\\(r < \sqrt{2}\\)) frente a la zona de aislamiento de vibraciones (\\(r > \sqrt{2}\\)).

---

## 📐 Fundamento Matemático y Físico

El sistema masa-resorte-amortiguador sometido a una fuerza periódica externa \\(F(t) = F_0 \cos(\omega t)\\) se rige por la ecuación diferencial de segundo orden:

\\[m \ddot{x}(t) + c \dot{x}(t) + k x(t) = F_0 \cos(\omega t)\\]

### Parámetros Principales del Sistema

1. **Frecuencia Natural no Amortiguada (\\(\omega_n\\)):**
   \\[\omega_n = \sqrt{\frac{k}{m}} \quad [\text{rad/s}], \qquad f_n = \frac{\omega_n}{2\pi} \quad [\text{Hz}]\\]

2. **Razón de Amortiguamiento (\\(\zeta\\)):**
   \\[\zeta = \frac{c}{c_{\text{crítico}}} = \frac{c}{2\sqrt{k m}}\\]

3. **Factor de Magnificación Dinámica (\\(M\\)):**
   \\[M(r, \zeta) = \frac{X}{\delta_{st}} = \frac{1}{\sqrt{(1 - r^2)^2 + (2\zeta r)^2}}\\]
   *Donde \\(r = \frac{\omega}{\omega_n}\\) es la razón de frecuencias entre el motor (\\(\omega\\)) y el sistema (\\(\omega_n\\)).*

4. **Ángulo de Desfase (\\(\phi\\)):**
   \\[\phi(r, \zeta) = \arctan\left(\frac{2\zeta r}{1 - r^2}\right) \quad [\text{grados}]\\]

5. **Transmisibilidad de Fuerza a la Fundación (\\(TR\\)):**
   \\[TR(r, \zeta) = \frac{F_{\text{transmitida}}}{F_0} = \sqrt{\frac{1 + (2\zeta r)^2}{(1 - r^2)^2 + (2\zeta r)^2}}\\]

---

## 💡 Las Tres Regiones Clave de la Dinámica Mecánica

| Región | Razón de Frecuencias (\\(r\\)) | Control Domante | Ángulo de Desfase (\\(\phi\\)) | Comportamiento Físico |
| :--- | :---: | :---: | :---: | :--- |
| **1. Rigidez** | \\(r \ll 1.0\\) | Resorte (\\(k\\)) | \\(\phi \approx 0^\circ\\) | El desplazamiento está en fase con la fuerza. Amplitud \\(X \approx F_0/k\\). |
| **2. Resonancia** | \\(r = 1.0\\) | Amortiguador (\\(c\\)) | \\(\phi = 90^\circ\\) | Pico máximo de vibración \\(M \approx 1/(2\zeta)\\). La fuerza equilibra al amortiguamiento. |
| **3. Inercia / Aislamiento** | \\(r > \sqrt{2} \approx 1.41\\) | Masa (\\(m\\)) | \\(\phi \approx 180^\circ\\) | Movimiento en oposición de fase. Se logra **aislamiento de vibraciones** (\\(TR < 1\\)). |

---

## 🖥️ Estructura del Repositorio

```text
├── app.py                  # Código principal de la aplicación en Streamlit
├── requirements.txt        # Dependencias del proyecto para Python
├── README.md               # Documentación y guía del proyecto
└── LEEME.txt               # Instrucciones rápidas para ejecución local
