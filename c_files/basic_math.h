// https://www.transmissionzero.co.uk/computing/building-dlls-with-mingw/

#ifndef BASICMATH_DLL_H
#define BASICMATH_DLL_H


#ifdef __cplusplus
extern "C"
{
#endif


// ADD_EXPORTS should only be defined when creating DLL
#ifdef ADD_EXPORTS
  #define ADDAPI __declspec(dllexport)
#else
  #define ADDAPI __declspec(dllimport)
#endif

// Declare Add(a, b) function
int ADDAPI SumInt(int a, int b);


#ifdef __cplusplus
}
#endif

#endif