import { formatDistance } from "date-fns";

// funciones de procesamiento y conversion de los datos
export function date_element(created_on) {
    console.log(Date(created_on.toDate()));
    return new Date(created_ont.toDate());
}

export function relativeDate(value) {
    return formatDistance(new Date(value), new Date());
}

