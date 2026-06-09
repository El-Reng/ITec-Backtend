# ITec-Backtend

Práctico 2: Pydantic 

En el práctico 1 dejamos un crud funcional en memoria, guardando datos en un diccionario. Para este práctico vamos a seguir por las mismas líneas, pero agregando pydantic para la validación de tipos y restricciones.

Para este segundo práctico la idea es que me entreguen una aplicación de FastAPI con un crud en memoria que incluya:
- Esquemas de pydantic para la estructura de los diccionarios (equivalente a la tabla en db).
- Parámetros definidos con metadatos usando Annotated junto con Path() o Query(). Los mismos deben incluir restricciones   (mayor que, longitud máxima, etc...).
- Asimismo, los esquemas de pydantic también deben estar definidos con Annotated y usar Field().
- Los endpoints que reciban id como parámetro de ruta (path()) deben levantar un HTTPException() si no encuentra se encuentra coincidencia por id.
- Finalmente, los path operations deben incluir un response_model y, si aplicase, un responses.

Pueden trabajar a partir de lo que entregaron en el práctico anterior, sumandole todas estas features.