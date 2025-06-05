<template>
  <!-- Хедер -->
  <header class="flex items-center justify-between px-6 md:px-10 py-5 bg-[#1e1e1e] text-white border-b border-gray-700">
    <router-link to="/" class="text-2xl font-bold hover:text-violet-400">
  <span>Wan</span><span class="text-violet-500">dra</span>
</router-link>

    <nav class="space-x-4 text-sm font-medium flex flex-wrap justify-end md:flex">
      <router-link to="/" class="hover:text-violet-400">Главная</router-link>

      <template v-if="isAuthenticated">
        <router-link to="/profile" class="hover:text-violet-400">Профиль</router-link>
        <router-link v-if="isAdmin" to="/admin" class="hover:text-violet-400">Админ</router-link>
        <button @click="handleLogout" class="hover:text-violet-400">Выйти</button>
      </template>

      <template v-else>
        <router-link :to="{ query: { modal: 'login' } }" class="hover:text-violet-400">Войти</router-link>
        <router-link :to="{ query: { modal: 'register' } }" class="hover:text-violet-400">Регистрация</router-link>
      </template>

      <span class="cursor-pointer">🔍</span>
    </nav>
  </header>

  <section class="relative bg-[#1e1e1e] text-white overflow-hidden isolation-auto z-0 max-w-screen-2xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 md:gap-20 items-center px-6 md:px-20 py-12 md:py-16 mb-20">
    <div class="space-y-8 md:space-y-10">
      <span class="text-sm font-semibold tracking-widest text-violet-400">Откройте мир с нами</span>

      <h1 class="text-4xl sm:text-5xl md:text-7xl font-extrabold leading-snug">
        Создаём <br />
        <span class="underline decoration-violet-400 decoration-4">Незабываемые</span><br />
        Путешествия
      </h1>

      <p class="text-gray-300 max-w-lg text-base sm:text-lg md:text-xl leading-relaxed">
        Мы покажем вам лучшие уголки планеты — от величественных гор до бескрайних песков.
      </p>


      <div class="bg-[#2a2a2a] shadow-xl rounded-2xl md:rounded-full px-6 py-6 flex flex-col md:flex-row flex-wrap gap-4 md:gap-6 items-start md:items-center max-w-xl mt-4 md:mt-6">
        <div class="flex flex-col text-sm">
          <span class="text-gray-400 font-medium">Направление</span>
          <span class="text-white">Бали</span>
        </div>
        <div class="flex flex-col text-sm">
          <span class="text-gray-400 font-medium">Дата</span>
          <span class="text-white">26 марта, пятница</span>
        </div>
        <div class="flex flex-col text-sm">
          <span class="text-gray-400 font-medium">Цена</span>
          <span class="text-white">₽ 87,000</span>
        </div>
        <button
  @click="scrollToTours"
  class="bg-violet-500 hover:bg-violet-600 text-white rounded-full px-5 py-2 md:ml-auto shadow-lg transition"
>
  🔍
</button>
      </div>
    </div>


    <div class="flex gap-4 md:gap-6 items-center justify-center md:justify-end flex-wrap md:flex-nowrap">
      <div class="relative">
        <img
          src="@/assets/images/italy-g.png"
          alt="main"
          class="rounded-xl shadow-md object-cover w-[200px] h-[320px] md:w-[280px] md:h-[470px]"
        />
        <div class="absolute -top-3 -right-3 text-2xl md:text-3xl">✈️</div>
      </div>
      <div class="flex flex-col gap-4 md:gap-6">
        <img
          src="@/assets/images/paris-g.png"
          alt="top right"
          class="rounded-xl shadow-md object-cover w-[180px] h-[140px] md:w-[260px] md:h-[200px]"
        />
        <img
          src="@/assets/images/bb-g.png"
          alt="bottom right"
          class="rounded-xl shadow-md object-cover w-[180px] h-[140px] md:w-[260px] md:h-[200px]"
        />
      </div>
    </div>
  </section>
</template>

<script setup>

function scrollToTours() {
  const el = document.getElementById('tours')
  if (el) el.scrollIntoView({ behavior: 'smooth' })
}
import { isAuthenticated, logout, userRole } from '@/stores/auth'
import { useRouter } from 'vue-router'
import { computed } from 'vue'

const router = useRouter()
const isAdmin = computed(() => userRole.value === 'admin')

function handleLogout() {
  logout()
  router.push('/')
}
</script>