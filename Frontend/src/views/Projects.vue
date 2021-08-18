<template>
  <div>
    <router-link to="/">
      <bread-crumbs>- HOME</bread-crumbs>
    </router-link>
    <moving-title>PROJECTS</moving-title>

    <div class="projects__inner">
      <!-- <div class="cards"> -->
        <!--  ПОПРОБОВАТЬ ВСТАВИТЬ ДАННЫЕ ИЗ БЭКЕНДА В ЭТУ КАРТОЧКУ ЕСЛИ НЕ ПОЛУЧАЕТСЯ ВСТАВИТЬ ИХ В КОМПОНЕНТ
          
          
          <div class="card">
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <div class="card__inner">
            <div
              class="card__face card__face--front"
              style="background: linear-gradient(360deg, #9ebd13 0%, #008552 100%);"
            >
              <h1>developer card</h1>
            </div>
            <div class="card__face card__face--back">
              <h1 class="backside__title">backside info</h1>
              <p class="backside__info">
                carblok - multi-page online store on auto parts. My work: design
                and identity development. Layout of a multi-page site. Working
                with SEO
              </p>
              <p class="backside__stack">
                HTML/CSS/JS/WORDPRESS
              </p>

              <div class="backside__links">
                <a href="">Learn more</a>
                <div class="backside__icons">
                  <a href=""
                    ><fa class="fa-gh icon" :icon="['fab', 'github']"
                  /></a>
                  <a href=""
                    ><fa
                      class="fa-exl icon"
                      :icon="['fas', 'external-link-alt']"
                  /></a>
                </div>
              </div>
            </div>
          </div>
        </div> -->
        <work-card v-bind:works="works"></work-card>
      </div>
    </div>
  <!-- </div> -->
</template>

<script>

import WorkCard from "../components/WorkCard.vue";
import BreadCrumbs from "../components/UI/BreadCrumbs.vue";
import MovingTitle from "../components/UI/MovingTitle.vue";
import axios from "axios";

export default {
  name: "Home",
  components: {
    WorkCard,
    BreadCrumbs,
    MovingTitle,
  },
  data() {
    return {
      works: [],
    };
  },

  methods: {
    async fetchWorks() {
      try {
        const responce = await axios.get("http://127.0.0.1:8000/works/");
        this.works = responce.data;
        console.log(responce)
      } catch (e) {
        alert("error");
      }
    },
  },

  created() {
    this.fetchWorks();
  },

  mounted() {
    const content = document.querySelector(".container");
    let currenPos = window.pageYOffset;
    const callDistort = function() {
      const newPos = window.pageYOffset;
      const diff = newPos - currenPos;
      const speed = diff * 0.05;

      content.style.transform = "skewY(" + speed + "deg)";
      currenPos = newPos;
      requestAnimationFrame(callDistort);
    };
    callDistort();
  },
};
</script>
<style scoped lang="sass">
.container
  display: block

// .cards
//   display: flex
//   justify-content: space-around
//   align-items: center
//   flex-wrap: wrap
//   transition: transform 0.1s
//   will-change: transform
  
</style>
