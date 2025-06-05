<template>
  <section class="bg-[#1e1e1e] py-16 px-4 md:px-20 max-w-screen-2xl mx-auto text-white">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
      <!-- Текст -->
      <div>
        <p class="text-violet-500 font-semibold text-sm md:text-base mb-2">Почему выбирают нас?</p>
        <h2 class="text-3xl sm:text-4xl md:text-5xl font-extrabold leading-snug mb-6">
          Отправляйтесь в путешествие <br class="hidden sm:block" />с уверенностью и комфортом
        </h2>
        <p class="text-gray-400 mb-8 text-base sm:text-lg leading-relaxed">
          Мы предлагаем тщательно подобранные туры, чтобы каждое ваше путешествие стало особенным.
          Независимо от направления — будь то пляжный отдых, приключения или культурный тур — мы заботимся о вашем комфорте и безопасности.
        </p>
        <button class="bg-violet-500 hover:bg-violet-600 text-white font-semibold px-6 sm:px-8 py-3 sm:py-4 text-base sm:text-lg rounded-xl shadow-lg transition">
          О нас
        </button>
      </div>

      <!-- Фото -->
      <div class="relative rounded-xl overflow-hidden">
        <img
          src="@/assets/images/sea.png"
          alt="Море"
          class="rounded-xl shadow-xl object-cover w-full h-64 sm:h-[400px]"
        />
      </div>
    </div>

    <!-- Стата -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-8 sm:gap-10 mt-16 sm:mt-20 text-center">
      <div>
        <p class="text-3xl font-bold text-white">2</p>
        <p class="text-gray-400 mt-2 text-base">Года опыта</p>
      </div>
      <div>
        <p class="text-3xl font-bold text-white">3</p>
        <p class="text-gray-400 mt-2 text-base">Партнёрских направления</p>
      </div>
      <div>
        <p class="text-3xl font-bold text-white">38+</p>
        <p class="text-gray-400 mt-2 text-base">Довольных клиентов</p>
      </div>
    </div>
  </section>
</template>