# Apuntes AZ-900
## Módulo: Descripción de los conceptos de la nube

### Conceptos clave aprendidos:

1. **Modelos de servicio de nube:**
   - On premise (Modelo local no en la nube): Todas las responsabilidades de seguridad, acceso, mantenimiento, conexión a la red, mantenimiento de los equipos recae sobre el proveedor.

   - IaaS: Infraestructura como servicio. El proveedor de la nube sólo se responsabiliza de que la infraestructura, el estado físico de los equipos y su conexión sea correcta. El resto recae sobre el cliente.

   - SaaS: Software como servicio. Los datos que se manejan, quien accede y los dispositivos recaen sobre el cliente. La identificación y el acceso es responsabilidad de proveedor y cliente, y por otra parte; las aplicaciones, los controles de internet, el sistema operativo, la infraestructura y la integridad física de los centros de datos, su conexión a internet y su mantenimiento recaen sobre el proveedor.

   - PaaS: Plataforma como servicio. Es un punto intermedio entre los otros 2 modelos. Comparten la responsabilidad de identificar a quien se da acceso a la plataforma, el software que vayan a utilizar y el control de la red. Los datos que se manejan, quien accede y los dispositivos recaen sobre el cliente y que el sistema funcione, la infraestructura  la integridad física de los centros de datos, su conexión a internet y su mantenimiento recaen sobre el proveedor.

1.1 A modo de resumen:
    Como cliente siempre será responsable de:
        - La información y los datos almacenados en la nube
        - Dispositivos que pueden conectarse a la nube (teléfonos móviles, equipos, etc.)
        - Las cuentas e identidades de las personas, los servicios y los dispositivos dentro de su entorno

    El proveedor de nube siempre es responsable de:
        - El centro de datos físico
        - La red física
        - Hosts físicos

    Lo que depende del tipo de servicio:
        - Sistemas operativos
        - Controles de red
        - APLICACIONES
        - Identidad y acceso
        - Infraestructura

2. **Modelos de despliegue:**
    A. Nube Pública (Public Cloud)
        Concepto: Alquilas espacio en los centros de datos de Microsoft (Azure). Es como vivir en un piso muy seguro dentro de un edificio gigante que es de todos, pero tu apartamento es solo tuyo.
        Tu entorno: Tus datos están en un servidor de Azure Storage o Azure SQL, no en tu oficina.
        Pros: No compras servidores (ahorras dinero inicial), escalas fácil si crece la base de datos, Microsoft se encarga de mantener el hardware.
        Contras: Pagas por lo que usas (puede salir caro si no gestionas bien).
    B. Nube Privada (Private Cloud)
        Concepto: Tienes tu propio centro de datos exclusivo. En tu caso, sería el servidor físico que está ahora mismo en la oficina de tu empresa.
        Tu entorno: Tu SQL Server local. Nadie más comparte ese hardware. Tú eres responsable de cambiarle el disco duro si se rompe, de ponerle aire acondicionado, de actualizarlo.
        Pros: Control total, seguridad física máxima (si eso importa para seguros).
        Contras: Muy caro de mantener, requiere equipo dedicado (IT), lento para escalar (si necesitas más potencia, compras otro servidor y tardas semanas en instalarlo).
    C. Nube Híbrida (Hybrid Cloud)
        Concepto: Una mezcla. Un pie en casa (oficina) y otro en la nube.
        Tu entorno (Muy probable en seguros):
        Los datos sensibles (Nombres de asegurados, DNI) se quedan en tu SQL Server local (Nube Privada) por temas legales/seguridad.
        Los datos de análisis (estadísticas de siniestralidad) se copian cada noche a Azure Data Lake (Nube Pública) para que tú hagas reportes rápidos.
        Usas una conexión privada (ExpressRoute) para unir ambos.
        Por qué es útil: Te permite modernizarte sin migrar todo de golpe. Es el estándar en empresas grandes actuales.
    D. Multinube 
        Concepto: Conjunto de nubes públicas. En un entorno multinube, se tiene que tratar con dos (o más) proveedores de nube pública y administrar recursos y seguridad en ambos entornos.

2.1. Tema Azure:
    Azure Arc
Azure Arc es un conjunto de tecnologías que ayudan a administrar el entorno en la nube. Azure Arc puede ayudar a administrar el entorno de nube, ya sea una nube pública únicamente en Azure, una nube privada en el centro de datos, una configuración híbrida o incluso un entorno multinube que se ejecuta en varios proveedores de nube a la vez.

    Azure VMware Solution
¿Qué ocurre si ya está establecido con VMware en un entorno de nube privada, pero quiere migrar a una nube pública o híbrida? Azure VMware Solution le permite ejecutar las cargas de trabajo de VMware en Azure con una integración y escalabilidad perfectas.

3. **Ventajas de la nube:**
   - Rapidez y facilidad de ampliación de servicios bajo demanda.
   - Responsabilidad compartida según el modelo de servicio contratado

## Apuntes Prácticos: Modelos Híbridos y Herramientas

### 1. Mi realidad actual (Modelo Híbrido)
- **Datos Críticos:** Están On-Premise (SQL Server local). Razón: Seguridad/Legal.
- **Aplicaciones Operativas:** Son SaaS (Proveedor externo). Razón: Rapidez/No mantener infraestructura.
- **Problema:** Necesito unir ambos mundos para analizar los datos juntos.

### 2. Conceptos Clave Aprendidos
- **Azure Arc:** No es un gestor de BD. Es una capa de gestión que permite controlar servidores locales desde el portal de Azure. Me permitiría aplicar políticas de seguridad a mi SQL local sin mover los datos.
- **Azure VMware:** Solución para migrar entornos VMware completos a Azure sin reescribir código. Útil en grandes migraciones "Lift & Shift".
- **Diferencia IaaS vs PaaS en mi caso:** 
  - Si migro a IaaS (VM en Azure): Seguiría teniendo que parchear Windows y gestionar backups.
  - Si migro a PaaS (Azure SQL): Microsoft gestiona todo, yo me enfoco en las consultas. **Esto es mi objetivo.**

### 3. Reflexión Personal
Mi empresa está en una transición típica. Mi valor futuro estará en diseñar pipelines que conecten nuestro SQL local (On-Prem) con servicios de análisis en la nube (PaaS), eliminando los procesos manuales actuales.

