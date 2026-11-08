# Clonar, actualizar y documentar el repositorio

## Primera descarga

1. Instala Git y confirma que puedes acceder a GitHub.
2. Clona el repositorio:

   ```powershell
   git clone https://github.com/Ericklies/develcd9614709.git
   cd develcd9614709
   ```

3. Comprueba que estás en `main` y que el proyecto está actualizado:

   ```powershell
   git switch main
   git pull origin main
   ```

## Actualización del clon

Antes de comenzar a trabajar, ejecuta desde la carpeta del repositorio:

```powershell
git switch main
git pull origin main
```

Si ya estás trabajando en una rama, guarda o confirma tus cambios antes de cambiar de rama. Actualiza `main` y luego integra sus cambios en tu rama de trabajo.

## Evidencia de cada integrante

Después de un `git pull origin main` exitoso, toma una captura donde se vean el comando y su resultado en la terminal. Guarda la imagen en:

```text
docs/screenshots/<nombre_integrante>.png
```

Usa un nombre corto y reconocible, por ejemplo `erick.png`. Añade la captura a tu Pull Request junto con los cambios del proyecto. No incluyas tokens, contraseñas ni información privada en la imagen.