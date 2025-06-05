<template>
  <section class="bg-[#1e1e1e] py-16 md:py-20 px-4 md:px-20 text-white">
    <div class="text-center mb-12">
      <p class="text-violet-500 font-semibold text-sm md:text-base">Посетите!</p>
      <h2 class="text-3xl sm:text-4xl font-extrabold">Доступные <span class="text-violet-500">туры</span></h2>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 md:gap-10">
      <div v-for="card in destinations" :key="card.id" class="bg-[#2b2b2b] rounded-3xl shadow-xl overflow-hidden transition hover:scale-[1.02]">
        <img :src="card.image" :alt="card.name" class="w-full h-48 sm:h-56 object-cover" />
        <div class="p-5 md:p-6 space-y-3">
          <div class="flex flex-wrap items-center gap-2 text-sm text-gray-300">
            <span class="bg-yellow-200 text-yellow-900 px-2 py-1 rounded-full">⭐ {{ card.rating }}</span>
            <span>{{ card.reviews }} отзыва</span>
          </div>
          <h3 class="text-lg md:text-xl font-bold text-white">{{ card.name }}</h3>
          <p class="text-violet-400 font-semibold">₽ {{ card.price }} <span class="text-gray-400 font-normal">/ с человека</span></p>
          <div class="flex flex-wrap gap-3 text-gray-400 text-sm">
            <span>🕓 {{ pluralizeDays(card.days) }}</span>
            <span>👥 {{ card.groupSize }}+</span>
            <span>📍 {{ card.country }}</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';

function pluralizeDays(n) {
  const mod10 = n % 10;
  const mod100 = n % 100;
  if (mod10 === 1 && mod100 !== 11) return `${n} день`;
  if (mod10 >= 2 && mod10 <= 4 && (mod100 < 10 || mod100 >= 20)) return `${n} дня`;
  return `${n} дней`;
}

const destinations = ref([]);

async function fetchTours() {
  try {
    const response = await fetch('/api/tours');
    const data = await response.json();
    destinations.value = data;
  } catch (err) {
    console.error('Failed to fetch tours:', err);
  }
}

onMounted(fetchTours);
</script>