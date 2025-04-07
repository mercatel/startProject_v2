<template>
  <client-only>
    <div>{{ auth.getUser }}</div>
  </client-only>
</template>

<script setup>
definePageMeta({
  requiresAuth: "auth"
})



const auth = useAuthStore()
</script>

<style scoped>

</style>