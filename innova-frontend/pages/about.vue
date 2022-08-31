<template>
  <div class="container-md">
    <div>
      <h2>¿Quiénes somos?</h2>
      <br>
      <p class="text-justify">
        El Centro de Capacitación Técnica Innova es un Organismo Técnico de
        Capacitación acreditado por el Servicio Nacional de Capacitación y
        Empleo (SENCE), bajo resolución del registro nacional N°3452. Nuestra
        empresa se encuentra enfocada a entregar servicios de capacitación de
        calidad a Instituciones públicas y privadas basado en la Norma Chile
        NCH2728 2015 por ASR Certificaciones. Nuestra institución entrega un
        servicio de educación, capacitación y formación de trabajadores,
        empresarios y personas en general, que requieran nuestros servicios bajo
        la formación de excelencia y calidad, incorporando un staff de relatores
        con sólida formación continua.
      </p>
    </div>
    <div class="div-margin-element">
      <p>Innova esta certificado por:</p>

      <div class="content-element">
        <div class="content-card-img">
            <v-img class="img-desing" src="../static/asr.png" />
          <p>Certificado por ASR Certificaciones</p>
        </div>
        <div class="content-card-img">
            <v-img class="img-desing" src="sence.jpg" />

          <p>Acreditada por SENCE</p>
        </div>
      </div>
    </div>

    <div class="div-margin-element">
      <h2>Experiencia</h2>
      <br>
      <p  class="text-justify">
        El Centro de Capacitación Técnica Innova ha impartido cursos de diversas
        áreas desde el año 2015 en adelante modalidad presencial y en modalidad
        sincrónica y asincrónica a lo largo de todo el país a funcionarios del
        área de salud, administración, municipalidades, emprendedores, programas
        sociales, oficios, entre otros.
      </p>
    </div>
  </div>
</template>

<script>
export default {};
</script>


<style lang="scss" scoped>
.container-md {
  width: 80%;
  margin: 0 auto;
  margin-top: 40px;
}

.img-desing {
  width: 100px;
  object-fit: cover;
}

.content-card-img {
  display: flex;
  width: 200px;
  margin-right: 20px;
}

.div-margin-element {
  max-width: 800px;
  margin-top: 50px;
}

.content-element {
  display: flex;
  align-items: center;
}
</style>