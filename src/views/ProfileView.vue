<template>
  <div class="min-h-screen bg-zinc-900 text-white">
    <header class="flex items-center justify-between px-10 py-5 bg-zinc-800 text-white border-b border-zinc-700">
      <router-link to="/" class="text-2xl font-bold hover:text-violet-400">
        <span>Wan</span><span class="text-violet-500">dra</span>
      </router-link>
      <nav class="space-x-6 font-medium flex flex-wrap justify-end md:flex">
        <router-link to="/" class="hover:text-violet-400">Главная</router-link>
        <button @click="logout" class="hover:text-violet-400">Выйти</button>
      </nav>
    </header>

    <section class="p-10 max-w-xl mx-auto text-center bg-zinc-800 shadow-xl rounded-xl mt-12 space-y-6">
      <h1 class="text-3xl font-bold text-violet-400">Добро пожаловать, {{ user.username }}!</h1>
      <div class="space-y-1 text-zinc-300">
        <p><span class="font-semibold">Email:</span> {{ user.email }}</p>
        <p><span class="font-semibold">Роль:</span> {{ user.role }}</p>
      </div>
      <div class="mt-8 text-left">
        <h2 class="text-xl font-semibold text-violet-400 mb-2">Забронированные туры</h2>
        <div v-if="bookings.length">
          <div v-for="booking in bookings" :key="booking.id" class="bg-zinc-700 p-4 rounded-lg mb-2">
            <p><span class="font-semibold">Тур:</span> {{ booking.tourName }}</p>
            <p><span class="font-semibold">Дата бронирования:</span> {{ new Date(booking.bookingDate).toLocaleDateString() }}</p>
            <p><span class="font-semibold">Статус оплаты:</span> {{ booking.paymentStatus }}</p>
          </div>
        </div>
        <p v-else class="text-zinc-400">У вас пока нет забронированных туров.</p>
      </div>
      <button @click="logout" class="mt-8 px-6 py-2 bg-gradient-to-r from-red-500 to-red-600 hover:from-red-600 hover:to-red-700 text-white font-semibold rounded-full shadow-md transition-all duration-200">Выйти из аккаунта</button>
    </section>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { onMounted, ref } from 'vue';
import { isAuthenticated, logout, token } from '@/stores/auth';

const router = useRouter();
const user = ref({});
const bookings = ref([]);

async function fetchUser() {
  try {
    const response = await fetch('/api/user', {
      headers: { 'Authorization': `Bearer ${token.value}` }
    });
    user.value = await response.json();
  } catch (err) {
    console.error('Failed to fetch user:', err);
    router.push({ path: '/', query: { modal: 'login' } });
  }
}

async function fetchBookings() {
  try {
    const response = await fetch('/api/bookings', {
      headers: { 'Authorization': `Bearer ${token.value}` }
    });
    bookings.value = await response.json();
  } catch (err) {
    console.error('Failed to fetch bookings:', err);
  }
}

onMounted(async () => {
  if (!isAuthenticated.value) {
    router.push({ path: '/', query: { modal: 'login' } });
  } else {
    await fetchUser();
    await fetchBookings();
  }
});

function logoutHandler() {
  logout();
  router.push('/');
}
</script>