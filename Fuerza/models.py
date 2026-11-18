from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Categoría")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class ProductoGym(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='productos',
        verbose_name="Categoría"
    )
    # 1. Texto
    nombre = models.CharField(max_length=120, verbose_name="Nombre del Artículo")
    marca = models.CharField(max_length=80, verbose_name="Marca")
    # 2. Numérico / Decimal
    precio_clp = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        verbose_name="Precio ($ CLP)"
    )
    stock = models.PositiveIntegerField(default=10, verbose_name="Stock Disponible")
    # 3. Fecha
    fecha_ingreso = models.DateField(verbose_name="Fecha de Ingreso")
    # 4. Booleano
    disponible = models.BooleanField(default=True, verbose_name="¿Disponible en catálogo?")
    # 5. Imagen
    imagen = models.ImageField(
        upload_to='productos/',
        blank=True,
        null=True,
        verbose_name="Imagen del Artículo"
    )

    class Meta:
        verbose_name = "Artículo de Gimnasio"
        verbose_name_plural = "Artículos de Gimnasio"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} (${self.precio_clp})"