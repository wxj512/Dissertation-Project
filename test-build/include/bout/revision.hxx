/// Information about the version of BOUT++
///
/// The build system will update this file on every commit, which may
/// result in files that include it getting rebuilt. Therefore it
/// should be included in as few places as possible

#ifndef BOUT_REVISION_H
#define BOUT_REVISION_H

// TODO: Make these all `inline` when we upgrade to C++17

namespace bout {
namespace version {
/// The git commit hash
#ifndef BOUT_REVISION
constexpr auto revision = "eae6e9dea74f55565498ee01cfe135351d22210a";
#else
// Stringify value passed at compile time
#define BUILDFLAG1_(x) #x
#define BUILDFLAG(x) BUILDFLAG1_(x)
constexpr auto revision = BUILDFLAG(BOUT_REVISION);
#undef BUILDFLAG1
#undef BUILDFLAG
#endif
} // namespace version
} // namespace bout

#endif // BOUT_REVISION_H
