# Gym Project - Catálogo de Equipamiento Deportivo

Aplicación web desarrollada en **Django 5.2 LTS** conectada a **MySQL Server 8.0**, diseñada para la gestión y consulta de inventario de artículos y equipamiento de gimnasio.

## Características Principales
- **Modelo Relacional 1:N:** Categorías (`Categoria`) y Artículos (`ProductoGym`) con soporte para imágenes (`ImageField` + `Pillow`).
- **CRUD Completo:** Listado con filtro por categoría y paginación, ficha de detalle, creación, edición y eliminación protegida.
- **Seguridad y Autenticación:** Sistema de inicio y cierre de sesión (`LoginRequiredMixin`) con control dinámico de botones en plantillas HTML.
- **Interfaz Responsiva:** Estilizada con Bootstrap 5, Bootstrap Icons y hojas de estilo personalizadas (`static/css/estilos.css`).

## Requisitos Previos
- Python 3.10 o superior
- MySQL Server 8.0 / MySQL Workbench

## Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd Gym_Project