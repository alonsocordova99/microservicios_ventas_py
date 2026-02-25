

export interface Paginated<T> {
    data: T[];
    total_paginas: number;
    pagina_actual: number;
    status: string;
}