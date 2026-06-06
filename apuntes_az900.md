# Apuntes AZ-900
## Módulo 1: Descripción de los conceptos de la nube

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

## Descripción del modelo basado en el consumo:

La informática en la nube funciona consiste en pagar por los recursos de TI que se usan y nada más. En lugar de comprar y mantener su propia infraestructura del centro de datos, se alquila la capacidad de proceso y el almacenamiento y se liberan esos recursos cuando haya terminado.

En el presupuesto de TI tradicional, puede escuchar los términos gastos de capital (CapEx) y gastos operativos (OpEx). CapEx hace referencia al gasto inicial en infraestructura física, como servidores, hardware de red y espacio en el centro de datos. OpEx hace referencia al gasto continuo en los servicios a lo largo del tiempo. Dado que paga por los servicios en la nube a medida que los consume, la informática en la nube se clasifica como un gasto operativo.


Con un centro de datos tradicional, se calculan las necesidades futuras de recursos de antemano. Si sobrestimas, gastarás de más en infraestructura que permanecerá inactiva. Subestimar y las aplicaciones sufren un rendimiento degradado. Corregir el problema significa ordenar, instalar y aprovisionar hardware adicional, energía y refrigeración.

En un modelo basado en la nube, ajustará los recursos para que coincidan con la demanda real. Agregue máquinas virtuales cuando necesite más capacidad; quítelos cuando baje la demanda. Solo paga por lo que usa, no por la capacidad inactiva. En la práctica, puede escalar horizontalmente durante la demanda máxima y reducir cuando disminuya el tráfico.

## Sugerencia para las IAs
Pruebe una de estas indicaciones en Copilot Chat:

"Explicar la responsabilidad compartida entre el entorno local, IaaS, PaaS y SaaS mediante un ejemplo concreto de aplicación empresarial".
Contexto: Aplicación de Gestión de Siniestros
Capa	On-Premises (Tu SQL Local)	IaaS (VM con SQL en Azure)	PaaS (Azure SQL Database)	SaaS (Salesforce/Dynamics)
Físico (Servidores, cables, electricidad)	🏢 TU EMPRESA	🔵 MICROSOFT	🔵 MICROSOFT	🔵 MICROSOFT
Virtualización	🏢 TU EMPRESA	🔵 MICROSOFT	🔵 MICROSOFT	🔵 MICROSOFT
Sistema Operativo	🏢 TU EMPRESA	🏢 TU EMPRESA	🔵 MICROSOFT	🔵 MICROSOFT
Actualizaciones de SO	🏢 TU EMPRESA	🏢 TU EMPRESA	🔵 MICROSOFT	🔵 MICROSOFT
Base de Datos	🏢 TU EMPRESA	🏢 TU EMPRESA	🔵 MICROSOFT	🔵 MICROSOFT
Backups de BD	🏢 TU EMPRESA	🏢 TU EMPRESA	🔵 MICROSOFT	🔵 MICROSOFT
Seguridad de Datos	🏢 TU EMPRESA	🏢 TU EMPRESA	🏢 TU EMPRESA*	🏢 TU EMPRESA*
Control de Acceso	🏢 TU EMPRESA	🏢 TU EMPRESA	🏢 TU EMPRESA	🏢 TU EMPRESA
Aplicación/Código	🏢 TU EMPRESA	🏢 TU EMPRESA	🏢 TU EMPRESA	🏢 TU EMPRESA
Nota: La seguridad de los datos siempre es responsabilidad del cliente. Lo que cambia es quién protege la infraestructura alrededor.

Ejemplo concreto aplicado a tu empresa:
    Escenario actual (On-Premise): Tienes una tabla Pólizas en SQL Server local.
        Si el servidor se queda sin espacio → Tú lo solucionas.
        Si Windows necesita un parche de seguridad crítico → Tú lo aplicas.
        Si quieres hacer backup a las 3 AM → Configuras tú SQL Agent.
        Si alguien hace backup completo de toda la DB y se va → Tú tienes que implementar cifrado.

    Escenario futuro (PaaS - Azure SQL): La misma tabla Pólizas en Azure SQL.
        Si necesitas más almacenamiento → Se escala automáticamente, no tocas nada.
        Parches de seguridad → Microsoft los aplica en ventana programada sin downtime.
        Backups → Ya están hechos (retención de 7-35 días por defecto).
        Cifrado transparente (TDE) → Activado por defecto.

    Lo que sigues haciendo tú en PaaS:
        Diseñar las tablas y consultas optimizadas.
        Gestionar usuarios que acceden a los datos.
        Proteger credenciales (API keys, passwords).
        Decidir qué datos se almacenan y cómo se clasifican


"Compare modelos públicos, privados, híbridos y multinube y, a continuación, recomiende la mejor opción para tres escenarios organizativos diferentes".

Tabla Comparativa
Modelo	Definición	Ventaja Principal	Desventaja Principal	Coste	Control
Pública	Recursos compartidos entre múltiples clientes	Escalable, barato, rápido	Menos personalización física	OpEx (pagas uso)	Bajo-Medio
Privada	Infraestructura exclusiva para ti	Control total, seguridad máxima	Caro, requiere equipo IT	CapEx (inversión inicial)	Máximo
Híbrida	Combinación pública + privada	Flexibilidad gradual	Complejo de gestionar	Mixto	Alto
Multi-nube	Usas Azure + AWS + Google simultáneamente	Evitas vendor lock-in	Muy complejo, coste alto	OpEx variable	Muy 

Recomendación para 3 Escenarios Empresariales
    Escenario A: Startup de InsurTech (España)
    Situación: 5 empleados, MVP de app, necesitan lanzar en 3 meses, presupuesto limitado.
    Datos: Historial de pólizas en desarrollo (no regulado aún).
    Recomendación: ✅ Nube Pública (Azure o AWS)
    Por qué:
        Sin inversión inicial (OpEx)
        Escalan con el crecimiento de usuarios
        No necesitan equipo IT dedicado
        Pueden empezar a PaaS inmediatamente

    Escenario B: Empresa de Seguros Tradicional (Tu caso actual)
    Situación: 500 empleados, datos sensibles, cumplimiento regulatorio (DPA, Ley Seguros), server room propio desde 2015.
    Datos: Información de asegurados, DNI, historiales médicos.
    Recomendación: ✅ Nube Híbrida
    Por qué:
        Datos críticos pueden quedarse On-Premise (cumplimiento legal)
        Datos analíticos/anónimos van a Azure para reportes rápidos
        Transición gradual sin romper operaciones actuales
        Puedes usar Azure Arc para empezar a gestionar lo local desde la nube

    Escenario C: Correduría Internacional (Sucursales en 10 países)
    Situación: Necesitan consistencia global, diferentes leyes locales, alto volumen de transacciones.
    Datos: Pólizas transfronterizas, pagos internacionales, cumplimiento GDPR + leyes locales.
    Recomendación: ✅ Multi-Nube Estratégica
    Por qué:
        Algunos países requieren datos almacenados localmente (ej: China, India)
        Evitan dependencia de un solo proveedor
        Pueden elegir mejor servicio por región (AWS en EE.UU., Azure en Europa)
        Mayor resiliencia si un proveedor falla


"Cree una comparación financiera de CapEx frente a OpEx para trasladar una carga de trabajo a un modelo de nube basado en el consumo".

Conceptos Clave
Término	Significado	¿Quién lo usa?	Ejemplo
CapEx	Capital Expenditure (Gasto de Inversión)	Empresas tradicionales	Comprar servidores físicos por 50k€
OpEx	Operational Expenditure (Gasto Operativo)	Cloud moderna	Pagar 500€/mes por servicios en Azure

Ejemplo Financiero: Migrar Sistema de Reportes de Siniestralidad
    Opción A: On-Premises (CapEx Predominante)
        Concepto	Año 1	Año 2	Año 3	Año 4	Año 5	TOTAL (5 años)
        Servidores (Compra)	25.000€	-	-	-	-	25.000€
        Almacenamiento SSD	8.000€	-	-	-	-	8.000€
        Licencias SQL Server	5.000€	-	-	-	-	5.000€
        Mantenimiento anual	-	2.000€	2.000€	2.000€	2.000€	8.000€
        Electricidad/Frío	1.500€	1.600€	1.700€	1.800€	1.900€	8.500€
        Personal IT (parcial)	10.000€	10.000€	10.000€	10.000€	10.000€	50.000€
        TOTAL	49.500€	13.600€	13.700€	13.800€	13.900€	104.500€
        Problemas ocultos:
        ⚠️ Obsolescencia hardware en 3-5 años
        ⚠️ Si crece el negocio, necesitas comprar más (nuevo CapEx)
        ⚠️ Depreciación fiscal (activos fijos)

    Opción B: Azure PaaS (OpEx Predominante)
        Concepto	Mes 1-12	Mes 13-24	Mes 25-36	Mes 37-48	Mes 49-60	TOTAL (5 años)
        Azure SQL Database	300€/mes	320€/mes	350€/mes	350€/mes	380€/mes	~21.200€
        Azure Data Factory	50€/mes	80€/mes	100€/mes	100€/mes	120€/mes	~5.400€
        Azure Storage	30€/mes	35€/mes	40€/mes	45€/mes	50€/mes	~2.400€
        Azure Monitor/Backup	20€/mes	20€/mes	25€/mes	25€/mes	30€/mes	~1.440€
        Personal IT (reducido)	5.000€/año	4.000€/año	4.000€/año	4.000€/año	4.000€/año	21.000€
        TOTAL	6.360€	6.000€	6.600€	6.780€	7.080€	~54.000€
        Ventajas Ocultas:
        ✅ Sin inversión inicial grande (cash flow mejorado)
        ✅ Escalas según necesidad (más uso = más pago, pero pagas lo que usas)
        ✅ Los gastos son deducibles como operativo al año siguiente
        ✅ Puedes cerrar el servicio cuando quieras sin perder "activos"

    Comparación Directa (5 años)
        Métrica	On-Premises	Azure PaaS	Diferencia
        Inversión inicial	38.000€	~2.000€ (configuración)	94% menos en Azure
        Coste total 5 años	104.500€	54.000€	49% ahorro en Azure
        Personal necesario	1 FTE dedicado	0.5 FTE compartido	50% reducción
        Flexibilidad	Baja (compres y espera)	Alta (escala en minutos)	Infinita en Azure
        Riesgo de obsolescencia	Alto (hardware caduca)	Bajo (Microsoft gestiona)	Menor riesgo en Azure
        ¿Cuándo tiene sentido quedarse On-Premises?
            Solo en estos casos:
                - Datos ultra-sensibles que no pueden salir del edificio por ley (algunos bancos públicos, defensa).
                - Carga de trabajo extremadamente constante 24/7 durante 5+ años (ahora mismo sale más caro en la nube).
                - Presupuesto disponible ahora pero sin capacidad de gasto operativo mensual (raro hoy día).

## FIN Módulo 1
