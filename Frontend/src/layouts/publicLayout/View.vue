<template>
    <transition appear name="fade" mode="out-in"
    enter-active-class="animate__animated animate__fadeInRight"
    leave-active-class="animate__animated animate__zoomOutRight"
    >
      <router-view />
    </transition>

     <!-- <router-view /> -->
  </template>

<script>
export default {
  name: 'Publicview',
  data() {
    return {
      visible: true,
    };
  },
  computed: {},
};
</script>