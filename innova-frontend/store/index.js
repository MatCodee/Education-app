import { setStore, getStore } from '@/config/utils'


const user = getStore('user')


export const state = () => ({

  // Esta es la informacion el usuario actual
  user_information: {},

  // Este es el formulario de las preguntas
  form_question: [],

  // desconocido
  btnobe: false,

  // login user google  
  loginUser: user,


  // desconocido
  current_id_week: -1,
  
  // desconocido
  file_class_upload: "",
  week_path: "",


  // desconocido
  counter: 0,

  // desconocido
  current_id_homework_send: -1,
  current_id_homework: -1,
  current_id_homework_course: -1,

  // desconocido
  slug_course: "",
  current_course: {},
  slug_course_proffesor: "",


  // Esta es la informacion de usuario que se va a guardar temporalmente hasta que se inicie session
  UserInfo: {
    username: "",
    email: "",
    fullname: "",
  },
  drawer: false,

  // cantidad de cursos que desea comprar 
  cart: {
    courses: [],
  },

  // informacion del formulario
  form: {},

})

export const mutations = {
  increment(state) {
    state.counter++
  },
  setSlugProffesor(state, slug) {
    state.slug_course_proffesor = slug;
  },

  setSlug(state, slug) {
    state.slug_course = slug;
  },

  removeSlugProffesor(state) { state.slug_course_proffesor = ''; },
  removeSlug(state) { state.slug_course = ''; },



  // Establecemos los valores 
  setUserInfo(state, username, email, fullname) {
    state.UserInfo.username = username;
    state.UserInfo.email = email;
    state.UserInfo.fullname = fullname;
  },
  // necesitamos una funcion para borrar los campos



  // funcion para devolver los cart
  initializeStoreCart(state) {
    if (localStorage.getItem('cart')) {
      state.cart = JSON.parse(localStorage.getItem('cart'));
    } else {
      localStorage.setItem('cart', JSON.stringify(state.cart));
    }
  },

  addToCart(state, course) {
    console.log(course);
    if (course) {
      const exist = state.cart.courses.filter(i => i.id === course.id);
      if (exist.length == 0) {
        state.cart.courses.push(course);
      }
      localStorage.setItem('cart', JSON.stringify(state.cart));
    }
  },
  removeToCart(state, course) {
    const exist = state.cart.courses.filter(i => i.id != course.id);
    state.cart.courses = exist
  },

  set_id_week(state,new_id) {
    state.current_id_week = new_id;
  },

  set_id_homework_send(state, new_id) {
    state.current_id_homework_send = new_id;
  },
  set_id_homework(state, new_id) {
    state.current_id_homework = new_id;
  },
  set_id_homework_course(state, new_id) {
    state.current_id_homework_course = new_id;
  },

  set_current_course(state,new_course) {
    state.current_course = new_course;
  },
  remove_current_course(state) {
    state.current_course = {};
  },

  // google set mutations
  setLoginUser(state, user) {
    state.loginUser = user
    setStore('user', user)
  },
  set_btn(state,new_value) {
    state.btnobe = new_value;
  },

  // cambio de almacenamiento
  week_delected(state,new_week) {
    state.week_path = new_week;
  },
  set_file_class_upload(state,value) {
    console.log(value);
    state.file_class_upload = value;
  },
  set_user_information(state,new_user_information) {
    state.user_information = new_user_information;
  },



  // informacion del formulario
  change_form(state,new_form) {
    //console.log("llamando a form desde el store")
    //console.log(new_form);
    
    state.form = new_form;
  },

  // agregar una pregunta al store
  add_question(state,question) {
    state.form_question.push(question);
  },
  asign_question_index_text(state,text_field,index) {
    state.form_question[index].question_text = text_field;
  },
  asign_question_index_choice(state,choice,index){
    state.form_question[index].choices_relations.push(choice)
  },
  delete_question(state,index) {
    let index_data = state.form_question.indexOf(index);
    state.form_question.splice(index_data,1);
  }

}

export const getters = {
  getLoginUserInfo(state) {
    return state.loginUser
  },
  get_user_information(state) {
    return state.user_information;
  } 
}
