<script setup>
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { userRole, token } from '@/stores/auth';

const router = useRouter();
const tours = ref([]);
const newTour = ref({
  title: '',
  description: '',
  price: '',
  country: '',
  city: '',
  type: '',
});

onMounted(async () => {
  if (userRole.value !== 'admin') {
    router.push('/');
  }
  await fetchTours();
});

async function fetchTours() {
  try {
    const response = await fetch('/api/tours', {
      headers: { 'Authorization': `Bearer ${token.value}` }
    });
    tours.value = await response.json();
  } catch (err) {
    console.error('Failed to fetch tours:', err);
  }
}

async function addTour() {
  if (newTour.value.title && newTour.value.description && newTour.value.price && newTour.value.country && newTour.value.city && newTour.value.type) {
    try {
      const response = await fetch('/api/tours', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token.value}`
        },
        body: JSON.stringify(newTour.value)
      });
      if (response.ok) {
        newTour.value = { title: '', description: '', price: '', country: '', city: '', type: '' };
        await fetchTours();
      }
    } catch (err) {
      console.error('Failed to add tour:', err);
    }
  }
}

async function deleteTour(id) {
  try {
    const response = await fetch(`/api/tours/${id}`, {
      method: 'DELETE',
      headers: { 'Authorization': `Bearer ${token.value}` }
    });
    if (response.ok) {
      await fetchTours();
    }
  } catch (err) {
    console.error('Failed to delete tour:', err);
  }
}
</script>

<template>
  <div class="min-h-screen bg-zinc-900 text-white p-10">
    <header class="flex items-center justify-between border-b border-zinc-700 pb-4 mb-6">
      <div class="flex flex-col md:flex-row md:items-center gap-1 md:gap-2">
        <router-link to="/" class="text-2xl font-bold hover:text-violet-400">
          <span>Wan</span><span class="text-violet-500">dra</span>
        </router-link>
        <div class="text-sm text-zinc-400">(Администратор: Рубан Никита)</div>
      </div>
      <router-link to="/" class="text-violet-400 hover:underline">На главную</router-link>
    </header>

    <section class="max-w-6xl mx-auto">
      <h2 class="text-xl font-bold mb-4 text-white">Список туров</h2>
      <div class="overflow-x-auto mb-10">
        <table class="w-full text-left border border-zinc-700">
          <thead class="bg-zinc-800">
            <tr>
              <th class="p-2 border border-zinc-700">ID</th>
              <th class="p-2 border border-zinc-700">Название</th>
              <th class="p-2 border border-zinc-700">Описание</th>
              <th class="p-2 border border-zinc-700">Цена</th>
              <th class="p-2 border border-zinc-700">Страна</th>
              <th class="p-2 border border-zinc-700">Город</th>
              <th class="p-2 border border-zinc-700">Тип отдыха</th>
              <th class="p-2 border border-zinc-700">Действия</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="tour in tours" :key="tour.id" class="hover:bg-zinc-800">
              <td class="p-2 border border-zinc-700">{{ tour.id }}</td>
              <td class="p-2 border border-zinc-700">{{ tour.name }}</td>
              <td class="p-2 border border-zinc-700">{{ tour.description }}</td>
              <td class="p-2 border border-zinc-700">{{ tour.price }}</td>
              <td class="p-2 border border-zinc-700">{{ tour.country }}</td>
              <td class="p-2 border border-zinc-700">{{ tour.city }}</td>
              <td class="p-2 border border-zinc-700">{{ tour.type }}</td>
              <td class="p-2 border border-zinc-700">
                <button @click="deleteTour(tour.id)" class="text-red-400 hover:underline">Удалить</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2 class="text-xl font-bold mb-4 text-white">Добавить новый тур</h2>
      <form @submit.prevent="addTour" class="grid grid-cols-1 md:grid-cols-2 gap-4 max-w-3xl">
        <input v-model="newTour.title" type="text" placeholder="Название" class="bg-zinc-800 text-white border border-zinc-600 p-2 rounded" />
        <input v-model="newTour.country" type="text" placeholder="Страна" class="bg-zinc-800 text-white border border-zinc-600 p-2 rounded" />
        <input v-model="newTour.city" type="text" placeholder="Город" class="bg-zinc-800 text-white border border-zinc-600 p-2 rounded" />
        <input v-model="newTour.price" type="number" placeholder="Цена" class="bg-zinc-800 text-white border border-zinc-600 p-2 rounded" />
        <input v-model="newTour.type" type="text" placeholder="Тип отдыха" class="bg-zinc-800 text-white border border-zinc-600 p-2 rounded" />
        <textarea v-model="newTour.description" placeholder="Описание" class="bg-zinc-800 text-white border border-zinc-600 p-2 rounded md:col-span-2"></textarea>
        <button type="submit" class="md:col-span-2 bg-violet-500 hover:bg-violet-600 text-white py-2 rounded transition">Добавить тур</button>
      </form>
    </section>
  </div>
</template>