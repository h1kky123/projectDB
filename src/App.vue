<template>
  <LoginModal
    v-if="route.query.modal === 'login'"
    @login="handleLoginSuccess"
    @close="router.push({ query: {} })"
  />
  <RegisterModal
    v-if="route.query.modal === 'register'"
    @close="router.push({ query: {} })"
  />
  <router-view />
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import LoginModal from '@/components/LoginModal.vue'
import RegisterModal from '@/components/RegisterModal.vue'

const route = useRoute()
const router = useRouter()

function handleLoginSuccess() {
  router.push({ query: {} })
}
</script>

<style>
body {
  background-color: #1e1e1e;
  color: white;
}
</style>