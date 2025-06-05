<template>
  <section
    class="bg-[#1e1e1e] text-white max-w-screen-2xl mx-auto px-6 md:px-20 py-16 md:py-20 grid grid-cols-1 md:grid-cols-2 gap-12 items-center"
  >
    <div class="w-full max-w-md mx-auto rounded-2xl overflow-hidden shadow-[0_20px_60px_rgba(0,0,0,0.4)]">
      <img
        src="@/assets/images/dubai.png"
        alt="Dubai"
        class="w-full h-auto object-cover"
      />
    </div>

    <div class="space-y-8 text-center md:text-left">
      <span class="text-sm md:text-base font-semibold tracking-wider text-violet-500">
        Почему выбирают нас?
      </span>

      <h2 class="text-3xl sm:text-4xl md:text-5xl font-extrabold leading-tight text-white">
        Планируйте путешествие с нами
      </h2>

      <ul class="space-y-6 text-sm sm:text-base md:text-lg">
        <li class="flex flex-col sm:flex-row items-center md:items-start gap-3 sm:gap-4">
          <div class="text-2xl">💰</div>
          <div>
            <h3 class="font-semibold text-white">Гарантия лучшей цены</h3>
            <p class="text-gray-400">Никаких скрытых платежей — только честные условия</p>
          </div>
        </li>
        <li class="flex flex-col sm:flex-row items-center md:items-start gap-3 sm:gap-4">
          <div class="text-2xl">📅</div>
          <div>
            <h3 class="font-semibold text-white">Гибкий график</h3>
            <p class="text-gray-400">Подберём дату, удобную именно вам</p>
          </div>
        </li>
        <li class="flex flex-col sm:flex-row items-center md:items-start gap-3 sm:gap-4">
          <div class="text-2xl">📍</div>
          <div>
            <h3 class="font-semibold text-white">Проверенные маршруты</h3>
            <p class="text-gray-400">Безопасно и интересно — от гор до океанов</p>
          </div>
        </li>
      </ul>
    </div>
  </section>
</template>