#pragma once
#include <string>
#include <boost/utility/string_view.hpp>
#include "utils.hpp"

namespace fuzz {
percent ratio(const boost::wstring_view& s1, const boost::wstring_view& s2, percent score_cutoff = 0);
percent partial_ratio(boost::wstring_view s1, boost::wstring_view s2, percent score_cutoff = 0);

percent token_sort_ratio(const boost::wstring_view& a, const boost::wstring_view& b, percent score_cutoff = 0);
percent partial_token_sort_ratio(const boost::wstring_view& a, const boost::wstring_view& b, percent score_cutoff = 0);

percent token_set_ratio(const boost::wstring_view& s1, const boost::wstring_view& s2, percent score_cutoff = 0);
percent partial_token_set_ratio(const boost::wstring_view& s1, const boost::wstring_view& s2, percent score_cutoff = 0);

percent token_ratio(const boost::wstring_view& s1, const boost::wstring_view& s2, percent score_cutoff = 0);
percent partial_token_ratio(const boost::wstring_view& s1, const boost::wstring_view& s2, percent score_cutoff = 0);

percent WRatio(const boost::wstring_view& s1, const boost::wstring_view& s2, percent score_cutoff = 0);
}
