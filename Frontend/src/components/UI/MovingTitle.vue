<template>
  <div class="header">
    <div data-speed="2" class="title parallaxer"><slot></slot></div>
  </div>
</template>

<script>
export default {
  mounted() {
    document.addEventListener("mousemove", parallax);
    function parallax(e) {
      this.querySelectorAll(".parallaxer").forEach((parallaxer) => {
        const speed = parallaxer.getAttribute("data-speed");

        const x = (window.innerWidth - e.pageX * speed) / 100;
        const y = (window.innerHeight - e.pageY * speed) / 100;

        parallaxer.style.transform = `translateX(${x}px) translateY(${y}px)`;
      });
    }
  },
};
</script>

<style lang="sass" scoped>
.header
  display: flex
  justify-content: center
  margin-top: 10px
  margin-bottom: 70px

.title
  font-weight: 300
  font-size: 70px
  color: black
</style>
