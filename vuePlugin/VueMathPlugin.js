export default {
    install: function (Vue) {
        // 自定义指令square v-square
        Vue.directive('square', function (el, binding) {
            el.innerHTML = Math.pow(binding.value, 2)
        });
        Vue.directive('sqrt',function(el,binding){
            el.innerHTML = Math.sqrt(binding.value)
        });
        // sin
        Vue.directive('sin',function(el,binding){
            el.innerHTML = Math.sin(binding.value)
        });
        // cos
        Vue.directive('cos',function(el,binding){
            el.innerHTML = Math.cos(binding.value)
        });
        // tan
        Vue.directive('tan',function(el,binding){
            el.innerHTML = Math.tan(binding.value)
        });
    }
}

