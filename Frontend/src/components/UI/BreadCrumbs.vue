<template>
  <div class="home"><slot></slot></div>
</template>

<script>
export default {};
</script>

<style lang="sass" scoped>
.home
  position: absolute
  top: 35px
  text-decoration: none
  color: #c7c7c7
  font-size: 12px
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
</style>
