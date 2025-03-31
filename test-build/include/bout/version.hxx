/// Information about the version of BOUT++
///
/// The build system will update this file at configure-time

#ifndef BOUT_VERSION_H
#define BOUT_VERSION_H

// TODO: Make these all `inline` when we upgrade to C++17

namespace bout {
namespace version {
/// The full version number
constexpr auto full = "5.1.2";
/// The major version number
constexpr int major = 5;
/// The minor version number
constexpr int minor = 1;
/// The patch version number
constexpr int patch = 2;
/// The version pre-release identifier
constexpr auto prerelease = "5.1.2";
/// The full version number as a double
constexpr double as_double = 5.12;
} // namespace version
} // namespace bout

#endif // BOUT_VERSION_H
