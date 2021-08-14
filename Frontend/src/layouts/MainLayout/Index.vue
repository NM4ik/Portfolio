<template>
    <div class="container">
      <pub-bar class="bar" />
      <pub-view />
    </div>
</template>


<script>
export default {
  name: 'Publiclayout',
  components: {
    PubBar: () => import(/* webpackChunkName: 'public-appbar' */ './AppBar'),
    PubView: () => import(/* webpackChunkName: 'public-view' */ './View'),
  },
};
</script>

<style lang="sass" scoped>
</style>