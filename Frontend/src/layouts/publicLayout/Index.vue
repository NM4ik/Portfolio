<template>
  <div class="container mainPage__wrapper">
    <pub-bar class="bar" />
    <pub-social class="social" />
    <pub-view />
  </div>
</template>


<script>
export default {
  name: 'Publiclayout',
  components: {
    PubBar: () => import(/* webpackChunkName: 'public-appbar' */ './AppBar'),
    PubSocial: () => import(/* webpackChunkName: 'public-socialBar' */ './SocialBar'),
    PubView: () => import(/* webpackChunkName: 'public-view' */ './View'),
  },
};
</script>


<style lang="sass">
  .social
    position: absolute
    left: 0
    top: 0
    z-index: 100

  .mainPage__wrapper
    position: relative
    display: block
    height: 100vh

  @media (max-width: 1536px)
    .social
      left: 50px
      
</style>