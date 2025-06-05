<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { login } from '@/stores/auth';

const email = ref('');
const password = ref('');
const router = useRouter();
const error = ref('');

async function handleLogin() {
  try {
    await login(email.value, password.value);
    router.push({ path: '/', query: {} });
  } catch (err) {
    error.value = err.message;
  }
}

function closeModal() {
  router.push({ path: '/', query: {} });
}
</script>

<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 backdrop-blur-sm flex items-center justify-center z-50 px-4" @click.self="closeModal">
    <div class="bg-zinc-900 text-white rounded-2xl p-6 sm:p-8 w-full max-w-md shadow-2xl relative">
      <button class="absolute top-4 right-4 text-gray-400 hover:text-white text-2xl" @click="closeModal">&times;</button>
      <h2 class="text-2xl sm:text-3xl font-bold text-center mb-6 text-violet-500">Вход</h2>
      <form @submit.prevent="handleLogin" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-300 mb-1">Email</label>
          <input v-model="email" type="email" class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-2 text-white focus:ring-violet-500 focus:border-violet-500" placeholder="Введите email" />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-300 mb-1">Пароль</label>
          <input v-model="password" type="password" class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-2 text-white focus:ring-violet-500 focus:border-violet-500" placeholder="Введите пароль" />
        </div>
        <div v-if="error" class="text-red-400 text-sm">{{ error }}</div>
        <button type="submit" class="w-full bg-violet-500 hover:bg-violet-600 text-white font-semibold py-2 rounded-lg transition">Войти</button>
      </form>
      <p class="text-sm text-center mt-6 text-gray-400">
        Нет аккаунта? <router-link to="/register" class="text-violet-500 hover:underline">Зарегистрироваться</router-link>
      </p>
    </div>
  </div>
</template>