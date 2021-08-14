<template>
  <div class="link__item">
    <p>
      <slot></slot>
    </p>
  </div>
</template>

<script>
  export default {
    mounted(){
      const btn = document.querySelectorAll('.link__item');
      for(let i = 0; i<btn.length; i++){
        // console.log(btn[i])
        let move = btn[i];
        move.onmousemove = function(e){
          const x = e.pageX - move.offsetLeft;
          const y = e.pageY - move.offsetTop;
          move.style.setProperty('--x', x + 'px');
          move.style.setProperty('--y', y + 'px');
        }
      }
    }
  }
</script>

<style lang="sass" scoped>
  .link__item
    position: relative
    display: inline-flex
    color: black
    border: solid #FF9321
    align-items: center
    padding: 24px 74px
    overflow: hidden
    p
      position: relative
      z-index: 1
      font-weight: 600
    &::before
      content: ''
      position: absolute
      top: var(--y)
      left: var(--x)
      width: 0
      height: 0
      background: #FF9321
      border-radius: 50%
      transition: width 0.5s, height 0.5s
      transform: translate(-50%, -50%)
    &:hover::before
      width: 250px
      height: 250px 
</style>