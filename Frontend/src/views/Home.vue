<template>
  <div class="home__inner">
    <div class="gretting">
      <span class="background__gretting parallaxer" data-speed="2">HELLO</span>
      <span class="gretting__decription parallax" data-speed="5"
        >I am a novice programmer, designer and friendly neighbor
        <fa icon="hand-spock" class="hand__spock"
      /></span>
    </div>

    <!-- UI-components "MyButton" -->
    <div class="link">
      <router-link to="/about">
        <my-button>About me</my-button>
      </router-link>
      <router-link to="/projects">
        <my-button>Projects</my-button>
      </router-link>
      <a :href="require('../assets/images/Avatar.jpg')" download="Avatar.jpg"><my-button>Resume</my-button></a>
    </div>
  </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton";
export default {
  name: "Home",
  components: {
    MyButton,
  },
  data: () => ({
    arrowRight: require("@/assets/images/icons/arrowRight.svg"),
  }),
  mounted() {
    document.addEventListener("mousemove", parallax);
    function parallax(e) {
      this.querySelectorAll(".parallaxer").forEach((parallaxer) => {
        const speed = parallaxer.getAttribute("data-speed");

        const x = (window.innerWidth - e.pageX * speed) / 30;
        const y = (window.innerHeight - e.pageY * speed) / 30;

        parallaxer.style.transform = `translateX(${x}px) translateY(${y}px)`;
      });
    }
  },
};
</script>
<style scoped lang="sass">
.home__inner
  background-color: none
  align-items: center
  padding: 0 70px

.gretting
  display: flex
  align-items: center
  justify-content: center
  margin-bottom: 130px


.background__gretting
  top: 0
  margin-top: 70px
  color: #EDEDED
  font-weight: 700
  text-align: center
  font-size: 200px
  position: absolute

.gretting__decription
  margin-top: 80px
  color: black
  font-weight: 500
  text-align: center
  font-size: 80px
  position: relative

.hand__spock
  color: #FFBF40
  width: 60px
  height: 100%

.link
  display: flex
  justify-content: center
  align-items: center
  a
    text-decoration: none
    margin-right: 40px
  a:last-of-type
    margin: 0!important

.home
  // margin-left: 100px
  color: white
  h1
    letter-spacing: 3px
    font-size: 35px
  span
    letter-spacing: 3px
    font-size: 12px

.subtitle
  letter-spacing: 2px!important
</style>
