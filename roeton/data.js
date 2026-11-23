/* Criscolor RoeTÓN · datos del catálogo interactivo (generado). 17 referencias. Fotos: /roeton/productos/{ficha-hd|mini}/<EAN>.webp */
const TOTAL_REFS = 17;
const STAR_CODES = [];
const FAMILIES = [{"id": "cebos", "name": "Cebos y cola", "desc": "RoeTÓN Grano, RoeTÓN Fresh y cola para ratas y ratones.", "count": 3}, {"id": "adhesivas", "name": "Trampas adhesivas", "desc": "Trampas adhesivas y trampas libro, en tamaño normal y grande.", "count": 3}, {"id": "ratoneras", "name": "Ratoneras y trampas de madera", "desc": "Trampas de madera RoeTÓN para ratas y ratoneras de 2 y 3 agujeros.", "count": 6}, {"id": "jaulas", "name": "Jaulas trampa", "desc": "Jaulas trampa metálicas y de madera para capturar roedores sin veneno.", "count": 5}];
const CATALOG = [
{"c": "42669", "n": "RoeTÓN cola para ratas y ratones 125 g", "e": "8435621426694", "f": "cebos"},
{"c": "42733", "n": "RoeTÓN Fresh 150 g", "e": "8435621427332", "f": "cebos"},
{"c": "42734", "n": "RoeTÓN Grano 150 g", "e": "8435621427349", "f": "cebos"},
{"c": "42670", "n": "RoeTÓN trampa adhesiva ratas 2 uds", "e": "8435621426700", "f": "adhesivas"},
{"c": "42671", "n": "RoeTÓN trampa libro ratas", "e": "8435621426717", "f": "adhesivas"},
{"c": "43827", "n": "RoeTÓN trampa libro ratas grande", "e": "8435621438277", "f": "adhesivas"},
{"c": "42666", "n": "RoeTÓN trampa madera rata 17,5 x 8,3 cm", "e": "8435621426663", "f": "ratoneras"},
{"c": "42667", "n": "RoeTÓN trampa madera rata 12 x 6,2 cm", "e": "8435621426670", "f": "ratoneras"},
{"c": "42668", "n": "RoeTÓN trampa madera rata 10 x 4,5 cm 2 uds", "e": "8435621426687", "f": "ratoneras"},
{"c": "43096", "n": "Ratonera 2 agujeros 9 x 6 x 4 cm", "e": "8435621430967", "f": "ratoneras"},
{"c": "43097", "n": "Ratonera 2 agujeros 15,5 x 9,5 x 6,5 cm", "e": "8435621430974", "f": "ratoneras"},
{"c": "43139", "n": "Ratonera 3 agujeros 12,5 x 6 x 4 cm", "e": "8435621431391", "f": "ratoneras"},
{"c": "42413", "n": "Jaula trampa roedores 15 x 12,7 x 12,7 cm", "e": "8435621424133", "f": "jaulas"},
{"c": "42414", "n": "Jaula trampa roedores 30 x 12,7 x 12,7 cm", "e": "8435621424140", "f": "jaulas"},
{"c": "43168", "n": "Jaula trampa roedores 23,5 x 11 x 11 cm", "e": "8435621431681", "f": "jaulas"},
{"c": "45330", "n": "Jaula trampa roedores madera 29 x 12 x 12 cm", "e": "8435621453300", "f": "jaulas"},
{"c": "45331", "n": "Jaula trampa roedores madera 20 x 8 x 8 cm", "e": "8435621453317", "f": "jaulas"}
];
const MODELS = [
{"id": "r42669", "t": "RoeTÓN cola para ratas y ratones 125 g", "f": "cebos", "d": [], "v": [{"c": "42669", "a": {}}], "s": 0, "k": "42669"},
{"id": "r42733", "t": "RoeTÓN Fresh 150 g", "f": "cebos", "d": [], "v": [{"c": "42733", "a": {}}], "s": 0, "k": "42733"},
{"id": "r42734", "t": "RoeTÓN Grano 150 g", "f": "cebos", "d": [], "v": [{"c": "42734", "a": {}}], "s": 0, "k": "42734"},
{"id": "r42670", "t": "RoeTÓN trampa adhesiva ratas 2 uds", "f": "adhesivas", "d": [], "v": [{"c": "42670", "a": {}}], "s": 0, "k": "42670"},
{"id": "r42671", "t": "RoeTÓN trampa libro ratas", "f": "adhesivas", "d": [], "v": [{"c": "42671", "a": {}}], "s": 0, "k": "42671"},
{"id": "r43827", "t": "RoeTÓN trampa libro ratas grande", "f": "adhesivas", "d": [], "v": [{"c": "43827", "a": {}}], "s": 0, "k": "43827"},
{"id": "r42666", "t": "RoeTÓN trampa madera rata 17,5 x 8,3 cm", "f": "ratoneras", "d": [], "v": [{"c": "42666", "a": {}}], "s": 0, "k": "42666"},
{"id": "r42667", "t": "RoeTÓN trampa madera rata 12 x 6,2 cm", "f": "ratoneras", "d": [], "v": [{"c": "42667", "a": {}}], "s": 0, "k": "42667"},
{"id": "r42668", "t": "RoeTÓN trampa madera rata 10 x 4,5 cm 2 uds", "f": "ratoneras", "d": [], "v": [{"c": "42668", "a": {}}], "s": 0, "k": "42668"},
{"id": "r43096", "t": "Ratonera 2 agujeros 9 x 6 x 4 cm", "f": "ratoneras", "d": [], "v": [{"c": "43096", "a": {}}], "s": 0, "k": "43096"},
{"id": "r43097", "t": "Ratonera 2 agujeros 15,5 x 9,5 x 6,5 cm", "f": "ratoneras", "d": [], "v": [{"c": "43097", "a": {}}], "s": 0, "k": "43097"},
{"id": "r43139", "t": "Ratonera 3 agujeros 12,5 x 6 x 4 cm", "f": "ratoneras", "d": [], "v": [{"c": "43139", "a": {}}], "s": 0, "k": "43139"},
{"id": "r42413", "t": "Jaula trampa roedores 15 x 12,7 x 12,7 cm", "f": "jaulas", "d": [], "v": [{"c": "42413", "a": {}}], "s": 0, "k": "42413"},
{"id": "r42414", "t": "Jaula trampa roedores 30 x 12,7 x 12,7 cm", "f": "jaulas", "d": [], "v": [{"c": "42414", "a": {}}], "s": 0, "k": "42414"},
{"id": "r43168", "t": "Jaula trampa roedores 23,5 x 11 x 11 cm", "f": "jaulas", "d": [], "v": [{"c": "43168", "a": {}}], "s": 0, "k": "43168"},
{"id": "r45330", "t": "Jaula trampa roedores madera 29 x 12 x 12 cm", "f": "jaulas", "d": [], "v": [{"c": "45330", "a": {}}], "s": 0, "k": "45330"},
{"id": "r45331", "t": "Jaula trampa roedores madera 20 x 8 x 8 cm", "f": "jaulas", "d": [], "v": [{"c": "45331", "a": {}}], "s": 0, "k": "45331"}
];
