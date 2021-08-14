<template>
  <div class="skills__col">
    <div class="col__text">Knowledge and experience in the layout of landing pages and sites</div>
    <div class="col__img"><img src="images/bootstrap_logo.svg" alt=""></div>
  </div>
</template>

<script>
  export default {
    
  }
</script>

<style lang="sass" scoped>
.skills__col
  transition: 0.3s linear
  display: flex
  margin-bottom: 15px
  justify-content: space-between
  align-items: center
  background-color: #1C1C1C
  flex-basis: 22%
  height: 120px
  .col__text
    margin-left: 25px
    margin-right: 15px
    font-weight: 400
    font-size: 14px
    color: white
  .col__img
    margin-right: 25px
  &:hover
    transform: scale(1.05)
</style>