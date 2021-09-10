<template>
  <div>
    <div class="cards">
      <div class="card" v-for="work in works" :key="work.id">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <div class="card__inner" v-on:click="FlipCard()">
          <div
            class="card__face card__face--front"
            :style="work.background_color"
          >
            <h1>{{ work.title }}</h1>
          </div>
          <div class="card__face card__face--back">
            <h1 class="backside__title">backside info</h1>
            <p class="backside__info">
              {{ work.backside_subtitle }}
            </p>
            <p class="backside__stack">
              {{ work.backside_stack }}
            </p>

            <div class="backside__links">
              <a href="">Learn more</a>

              <div class="backside__icons">
                <a href=""
                  ><fa class="fa-gh icon" :icon="['fab', 'github']"
                /></a>
                <a href=""
                  ><fa class="fa-exl icon" :icon="['fas', 'external-link-alt']"
                /></a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["works"],
  data() {
    return {
    };
  },

  methods:{
    FlipCard(){
      const card = document.querySelectorAll(".card__inner");
      for (let i = 0; i < card.length; i++) {
        card[i].onclick = function(e) {
          card[i].classList.toggle("is-flipped");
        };
      }
    }
  },
};
</script>

<style lang="sass" scoped>
.cards
  display: flex
  justify-content: space-around
  align-items: center
  flex-wrap: wrap
  transition: transform 0.1s
  will-change: transform

.backside__title
  font-weight: 600
  letter-spacing: 3px
  font-size: 30px
  margin-top: 15px
  margin-bottom: 30px

.backside__info
  margin: 0 30px
  color: black
  text-align: left

.backside__stack
  margin: 55px 0
  font-weight: 500
  font-style: italic
  letter-spacing: 2px

.backside__links
  display: flex
  justify-content: space-between
  margin: 0 30px 60px 30px
  >a
    text-decoration: none
    color: black
    position: relative
    &::before
      right: 0
      content: ''
      bottom: 0
      position: absolute
      width: 0%
      bottom: -3px
      height: 1px
      background-color: #FF9321
      transition: 0.2s
    &:hover::before
      width: 100%
      left: 0
  .backside__icons
    .icon
      margin-right: 15px
      width: 21px
      height: 21px
      color: #FF9321

.card__inner
  width: 100%
  height: 100%
  transition: transform 1s
  transform-style: preserve-3d
  cursor: pointer
  position: relative

.card__inner.is-flipped
  transform: rotateY(180deg)

.card__face
  color: white
  position: absolute
  width: 100%
  height: 100%
  -webkit-backface-visibility: hidden
  backface-visibility: hidden
  overflow: hidden
  box-shadow: 4px 4px 8px 0px rgba(255, 214, 0, 0.2)


.card__face--front
  display: flex
  background: linear-gradient(180deg, #d53369 0%, #daae51 100%)
  z-index: -1
  align-items: center
  justify-content: center
  h2
    color: white
    font-size: 32px

.card__face--back
  display: flex
  flex-direction: column
  justify-content: space-between
  background-color: white
  transform: rotateY(180deg)
  color: black

.card
  color: white
  position: relative
  width: 400px
  height: 400px
  text-align: center
  display: flex
  align-items: center
  justify-content: center
  overflow: hidden
  perspective: 1000px
  margin-bottom: 60px
  span
    transition: 0.5
    opacity: 0
    z-index: 2
  &:hover span
    opacity: 1

.card span:nth-child(1)
  position: absolute
  top: 0
  left: 0
  width: 100%
  height: 3px
  background: linear-gradient(to right, transparent, #FF9321)
  animation: animate1 1.6s linear infinite

@keyframes animate1
  0%
    transform: translateX(-100%)
  100%
    transform: translateX(100%)

.card span:nth-child(2)
  position: absolute
  top: 0
  right: 0
  height: 100%
  width: 3px
  background: linear-gradient(to bottom, transparent, #FF9321)
  animation: animate2 1.6s linear infinite
  animation-delay: 0.8s

@keyframes animate2
  0%
    transform: translateY(-100%)
  100%
    transform: translateY(100%)

.card span:nth-child(3)
  position: absolute
  bottom: 0
  left: 0
  width: 100%
  height: 3px
  background: linear-gradient(to left, transparent, #FF9321)
  animation: animate3 1.6s linear infinite

@keyframes animate3
  0%
    transform: translateX(100%)
  100%
    transform: translateX(-100%)

.card span:nth-child(4)
  position: absolute
  top: 0
  left: 0
  height: 100%
  width: 3px
  background: linear-gradient(to top, transparent, #FF9321)
  animation: animate4 1.6s linear infinite
  animation-delay: 0.8s

@keyframes animate4
  0%
    transform: translateY(100%)
  100%
    transform: translateY(-100%)
</style>
