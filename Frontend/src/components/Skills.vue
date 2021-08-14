<template>
  <div>
    <div class="skills__subtitle"><slot name="subtitle"></slot></div>
    <div class="skills__block"><slot name="skillcard"></slot></div>
  </div>
</template>

<script>
  export default {
    
  }
</script>

<style lang="sass" scoped>
.skills__block
  display: flex
  flex-wrap: wrap
  justify-content: space-between

.skills__subtitle 
  font-weight: 400
  font-size: 18px
  margin-top: 25px
  margin-bottom: 15px
</style>