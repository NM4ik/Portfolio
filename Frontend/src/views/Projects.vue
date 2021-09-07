<template>
  <div>
    <router-link to="/">
      <bread-crumbs>- HOME</bread-crumbs>
    </router-link>
    <moving-title>PROJECTS</moving-title>
    <div class="projects__inner">
      <div v-if="errored">
        <p>
          We're sorry, we're not able to retrieve works at the moment, please
          try back later
        </p>
      </div>
      <div v-if="loading">Loading...</div>
      <work-card v-bind:works="works"></work-card>
    </div>
  </div>
</template>

<script>
import WorkCard from "../components/WorkCard.vue";
import BreadCrumbs from "../components/UI/BreadCrumbs.vue";
import MovingTitle from "../components/UI/MovingTitle.vue";
import getAPI from "@/api/getAPI.js";

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
      loading: true,
      errored: false,
    };
  },

  methods: {
    async fetchWorks() {
      getAPI
        .get("works/")
        .then((response) => (this.works = response.data))
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
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

.projects__inner
  text-align: center

// .cards
//   display: flex
//   justify-content: space-around
//   align-items: center
//   flex-wrap: wrap
//   transition: transform 0.1s
//   will-change: transform
</style>
