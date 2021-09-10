<template>
  <div class="about__inner">
    <router-link to="/">
      <bread-crumbs>- HOME</bread-crumbs>
    </router-link>
    <moving-title>ABOUT ME</moving-title>
    <div class="container">
      <div class="catch__errors">
        <div v-if="errored">
          <p>
            We're sorry, we're not able to retrieve works at the moment, please
            try back later
          </p>
        </div>
        <div v-if="loading">Loading...</div>
      </div>
      <div class="description">
        <div class="text">
          <h1>WHO AM I</h1>
          <span
            >Lorem ipsum dolor sit amet, Arcu, sed nisi, mi, arcu libero
            phasellus tincidunt. Rhoncus, diam penatibus aliquet tellus, in
            rutrum augue. Pellentesque senectus risus consectetur et sed purus
            sed. Consectetur adipiscing elit. Egestas porttitor nulla nulla
            egestas odio pharetra egestas aliquet mollis. Arcu, sed nisi, mi,
            arcu libero phasellus tincidunt. Rhoncus, diam penatibus aliquet
            tellus, in rutrum augue. Pellentesque senectus risus consectetur et
            sed purus sed. Consectetur adipiscing elit. Egestas porttitor nulla
            nulla egestas odio pharetra egestas aliquet mollis. diam penatibus
            aliquet tellus, in rutrum augue. Pellentesque.</span
          >
        </div>
        <div class="image">
          <img src="@/assets/images/Avatar.jpg" alt="" />
          <div class="background"></div>
        </div>
      </div>

      <div class="skills">
        <div class="skills__title">Skills</div>
        <skills v-bind:skill="skill"> </skills>
      </div>
    </div>
  </div>
</template>

<script>
import BreadCrumbs from "../components/UI/BreadCrumbs.vue";
import MovingTitle from "../components/UI/MovingTitle.vue";
import SkillCard from "../components/UI/SkillCard.vue";
import Skills from "../components/Skills.vue";
import MyButton from "../components/UI/MyButton.vue";
import getAPI from "@/api/getAPI.js";

export default {
  name: "Home",
  components: {
    BreadCrumbs,
    MyButton,
    MovingTitle,
    SkillCard,
    Skills,
  },

  data() {
    return {
      skill: [],
      teches: [],
      info: [],
      loading: true,
      errored: false,
    };
  },

  methods: {
    async fetchSkills() {
      getAPI
        .get("skills/")
        .then((response) => {
          this.skill = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          alert("error");
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },

    async fetchPerson() {
      getAPI
        .get("person/")
        .then((response) => (this.info = response.data))
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
  },

  created() {
    this.fetchSkills();
    this.fetchPerson();
  },
};
</script>

<style lang="sass" scoped>
.skills__subtitle
  font-weight: 400
  font-size: 18px
  margin-top: 25px
  margin-bottom: 15px

.about__inner
  padding: 20px 90px

.description
  display: flex
  justify-content: space-between
  align-items: flex-start
  .image
    display: flex
    align-items: center
    justify-content: center
    img
      width: 300px
      height: 400px
      position: absolute
      z-index: 99
    .background
      width: 320px
      height: 420px
      background: #FF9321
      position: relative
  .text
    display: flex
    flex-direction: column
    h1
      font-weight: 600
      font-size: 140px
      color: #B1B1B1
    span
      line-height: 1.5
      font-size: 20px
      font-weight: 400
      color: black
      margin-right: 100px

.catch__errors
  text-align: center

.skills__title
  margin-top: 100px
  font-weight: 600
  font-size: 24px
</style>
