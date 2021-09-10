<template>
  <div>
    <div v-for="sk in skill" :key="sk.id">
      <div class="skills__subtitle">{{ sk.name }}</div>
      <div class="skils_block">
        <div class="skills__col" v-for="tech in sk.tech_id" :key="tech.tech_id">
          <div class="col__text">{{ tech.description }}</div>
          <div class="col__img">
            <img :src="tech.image" alt="" />
            <!-- Разобраться с загрузкой картинки -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["skill"],
};
</script>

<style lang="sass" scoped>
.skils_block
  display: flex
  flex-wrap: wrap
  justify-content: space-beetwen

.skills__col
  margin: 10px
  padding: 10px
  transition: 0.3s linear
  display: flex
  margin-bottom: 15px
  justify-content: space-between
  align-items: center
  background-color: #1C1C1C
  flex-basis: 31%
  height: 120px
  .col__text
    margin-left: 15px
    margin-right: 15px
    font-weight: 400
    font-size: 14px
    color: white
  .col__img
    // display: none
    // justify-content: center
    // align-items: center
    // margin-right: 25px
    // width: 90%
    height: 100%
    padding: 15px
    img
      height:100%
  &:hover
    transform: scale(1.05)

.skills__block
  display: flex
  flex-wrap: wrap
  justify-content: space-between

.skills__subtitle
  color: black
  font-weight: 400
  font-size: 18px
  margin-top: 25px
  margin-bottom: 15px
</style>
