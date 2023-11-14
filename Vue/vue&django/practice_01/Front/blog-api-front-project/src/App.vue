
<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink :to="{name: 'main'}">Main</RouterLink> | 
        <RouterLink :to="{name: 'posts'}">Posts</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>
.wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
  text-align: center ;
}

nav {
  background-color: gray;
  padding: 1rem;
}

nav a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

</style>
