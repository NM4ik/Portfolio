<template>
  <div>
    <router-link to="/">
      <bread-crumbs>- HOME</bread-crumbs>
    </router-link>
    <moving-title>PROJECTS</moving-title>
    <div class="projects__inner">
      <work-card v-bind:works="works"></work-card>
    </div>
  </div>
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
