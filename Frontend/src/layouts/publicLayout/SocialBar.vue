<template>
  <div class="social__inner">
    <div class="vl"></div>
    <ul class="social__media">
      <li class="social__item github"><a href=""><fa class="fa-gh icon" :icon="['fab', 'github']" /></a></li>
      <li class="social__item telegram"><a href=""><fa class="fa-tg icon" :icon="['fab', 'telegram']" /></a></li>
      <li class="social__item vkontakte"><a href=""><fa class="fa-vk icon" :icon="['fab', 'vk']" /></a></li>
      <li class="social__item instagram"><a href=""><fa class="fa-in icon" :icon="['fab', 'instagram']" /></a></li>
    </ul>
    <div class="vl"></div>
  </div>
</template>

<script>
export default {
  data: () => ({
    
  })
}
</script>

<style lang="sass" scoped>
  .vl
    border-left: 2px solid black
    flex-grow: 2
    height: 100%
    margin: 30px 0

  .social__inner
   display: flex
   flex-direction: column
   height: 100%
   justify-content: center
   align-items: center

  .social__media
    display: flex
    flex-direction: column
    justify-content: center
    align-items: center
    list-style: none
    li
      margin: 0x 

  .icon
    width: 24px
    height: 24px

  .social__item > a
    display: flex
    margin: 8px

  .social__item
    border-radius: 50%
    // border: 3px solid #FF9321
    background-color: #FF9321
    transition: all 0.3s
    cursor: pointer

  .social__media > li:not(:last-child)
    margin-bottom: 20px

  a
   color: white

  .github:hover
    box-shadow: 0px 0px 15px #FF9321
    .fa-gh
      color: white

  .telegram:hover
    border-color: black
    box-shadow: 0px 0px 15px #FF9321
    .fa-tg
      color: white

  .vkontakte:hover
    border-color: black
    box-shadow: 0px 0px 15px #FF9321
    .fa-vk
      color: white

  .instagram:hover
    border-color: black
    box-shadow: 0px 0px 15px #FF9321
    .fa-in
      color: white
  
</style>